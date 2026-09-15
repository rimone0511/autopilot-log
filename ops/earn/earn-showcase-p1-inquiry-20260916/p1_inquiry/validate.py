"""Input validation. Ambiguous or broken records fail closed to needs_human."""

from __future__ import annotations

import re
from datetime import datetime, timezone

# Showcase clock. Fixture INQ-S0-009 is intentionally after this instant.
AS_OF = datetime(2026, 9, 16, 12, 0, tzinfo=timezone.utc)

ALLOWED_CHANNELS = frozenset({"email", "form", "chat", "phone_note"})

# Fail-closed: these phrases always require a human. Not a classifier score.
RISK_KEYWORDS = (
    "返金",
    "苦情",
    "クレーム",
    "弁護士",
    "訴訟",
    "法的",
    "詐欺",
    "refund",
    "lawyer",
    "attorney",
    "lawsuit",
    "legal action",
    "complaint",
)

UNCLEAR_ONLY = frozenset(
    {
        "こんにちは",
        "はじめまして",
        "hello",
        "hi",
        "hey",
        "営業です",
        "資料希望",
        "?",
        "？",
    }
)

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PLACEHOLDER_NAMES = frozenset({"", "不明", "unknown", "n/a", "なし", "未記載"})


def _s(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_email(value: object) -> str:
    return _s(value).lower()


def normalize_phone(value: object) -> str:
    digits = re.sub(r"\D+", "", _s(value))
    if digits.startswith("81") and len(digits) >= 12:
        digits = "0" + digits[2:]
    return digits


def parse_received_at(value: object) -> datetime | None:
    raw = _s(value)
    if not raw:
        return None
    try:
        if raw.endswith("Z"):
            raw = raw[:-1] + "+00:00"
        dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def validate_record(record: dict, as_of: datetime | None = None) -> list[str]:
    """Return reason codes. Empty list means structurally usable (not yet unique)."""
    reasons: list[str] = []
    clock = as_of or AS_OF

    inquiry_id = _s(record.get("inquiry_id"))
    if not inquiry_id:
        reasons.append("MISSING_INQUIRY_ID")

    received = parse_received_at(record.get("received_at"))
    if not _s(record.get("received_at")):
        reasons.append("MISSING_RECEIVED_AT")
    elif received is None:
        reasons.append("UNPARSEABLE_RECEIVED_AT")
    else:
        if received > clock:
            reasons.append("FUTURE_RECEIVED_AT")

    channel = _s(record.get("channel")).lower()
    if channel not in ALLOWED_CHANNELS:
        reasons.append("UNKNOWN_CHANNEL")

    name = _s(record.get("name"))
    if name.lower() in PLACEHOLDER_NAMES:
        reasons.append("MISSING_NAME")

    email = normalize_email(record.get("email"))
    phone = normalize_phone(record.get("phone"))
    if not email and not phone:
        reasons.append("MISSING_CONTACT")
    if email and EMAIL_RE.match(email) is None:
        reasons.append("INVALID_EMAIL")
    if phone and not (10 <= len(phone) <= 11):
        reasons.append("INVALID_PHONE")

    subject = _s(record.get("subject"))
    if not subject:
        reasons.append("MISSING_SUBJECT")

    body = _s(record.get("body"))
    if not body:
        reasons.append("MISSING_BODY")
    if body and len(body) < 8:
        reasons.append("BODY_TOO_SHORT")
    if body.lower() in UNCLEAR_ONLY:
        reasons.append("UNCLEAR_INTENT")

    blob = f"{subject}\n{body}".lower()
    if any(keyword.lower() in blob for keyword in RISK_KEYWORDS):
        reasons.append("RISK_KEYWORD")

    return reasons
