"""Duplicate and identity matching. Unsure matches fail closed to needs_human."""

from __future__ import annotations

import re
import unicodedata
from typing import Iterable

from .validate import normalize_email, normalize_phone

# High overlap + shared contact => treat as the same thread (still human-held).
NEAR_DUPLICATE = 0.88
# Mid overlap, or high overlap without a shared contact => do not auto-accept.
AMBIGUOUS = 0.60


def _s(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_text(value: object) -> str:
    text = unicodedata.normalize("NFKC", _s(value)).lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def identity_keys(record: dict) -> dict[str, str]:
    email = normalize_email(record.get("email"))
    phone = normalize_phone(record.get("phone"))
    name = normalize_text(record.get("name"))
    company = normalize_text(record.get("company"))
    keys = {}
    if email:
        keys["email"] = email
    if phone and 10 <= len(phone) <= 11:
        keys["phone"] = phone
    if name:
        keys["name"] = name
    if company:
        keys["company"] = company
    if name and company:
        keys["name_company"] = f"{name}|{company}"
    return keys


def shingles(value: object, n: int = 2) -> set[str]:
    text = re.sub(r"\s+", "", normalize_text(value))
    text = re.sub(r"[。、．，,.!！?？:：;；'\"「」『』（）()\[\]/-]+", "", text)
    if not text:
        return set()
    if len(text) < n:
        return {text}
    return {text[i : i + n] for i in range(len(text) - n + 1)}


def jaccard(a: Iterable[str], b: Iterable[str]) -> float:
    left, right = set(a), set(b)
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def body_similarity(left: dict, right: dict) -> float:
    return jaccard(shingles(left.get("body")), shingles(right.get("body")))


def subject_similarity(left: dict, right: dict) -> float:
    return jaccard(shingles(left.get("subject")), shingles(right.get("subject")))


def shared_contact(left: dict, right: dict) -> list[str]:
    a, b = identity_keys(left), identity_keys(right)
    shared = []
    if "email" in a and a.get("email") == b.get("email"):
        shared.append("email")
    if "phone" in a and a.get("phone") == b.get("phone"):
        shared.append("phone")
    return shared


def weak_identity_overlap(left: dict, right: dict) -> bool:
    a, b = identity_keys(left), identity_keys(right)
    return bool(a.get("name_company") and a.get("name_company") == b.get("name_company"))


def compare_pair(newer: dict, older: dict) -> list[str]:
    """Compare newer against one earlier record. Empty = no duplicate signal."""
    reasons: list[str] = []
    contacts = shared_contact(newer, older)
    body = body_similarity(newer, older)
    subject = subject_similarity(newer, older)

    if "email" in contacts:
        reasons.append("EXACT_EMAIL_DUPLICATE")
    if "phone" in contacts:
        reasons.append("EXACT_PHONE_DUPLICATE")

    if body >= NEAR_DUPLICATE:
        if contacts:
            reasons.append("NEAR_DUPLICATE")
        else:
            reasons.append("AMBIGUOUS_SIMILARITY")
    elif body >= AMBIGUOUS and (contacts or weak_identity_overlap(newer, older)):
        reasons.append("AMBIGUOUS_SIMILARITY")

    # Same name+company with a different contact is never auto-accepted.
    if weak_identity_overlap(newer, older) and not contacts:
        reasons.append("AMBIGUOUS_IDENTITY")

    # De-dupe reason codes while keeping order.
    seen = set()
    ordered = []
    for reason in reasons:
        if reason not in seen:
            seen.add(reason)
            ordered.append(reason)
    return ordered


def find_duplicate_hits(record: dict, prior: list[dict]) -> list[dict]:
    hits = []
    for older in prior:
        reasons = compare_pair(record, older)
        if reasons:
            hits.append(
                {
                    "other_id": _s(older.get("inquiry_id")),
                    "reasons": reasons,
                    "body_similarity": round(body_similarity(record, older), 3),
                    "subject_similarity": round(subject_similarity(record, older), 3),
                    "shared_contact": shared_contact(record, older),
                }
            )
    return hits
