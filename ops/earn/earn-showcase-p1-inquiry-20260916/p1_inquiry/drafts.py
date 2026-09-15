"""Template reply stub. SAMPLE/SYNTHETIC only. Never sent."""

from __future__ import annotations

STUB_LABEL = "SAMPLE / 合成下書き"
STUB_BANNER = (
    "【SAMPLE / 合成下書き】この文面は見本です。送信しないでください。"
    "自動送信機能はありません。"
)


def draft_for(record: dict, reasons: list[str]) -> dict:
    name = (record.get("name") or "（名前なし）").strip()
    subject = (record.get("subject") or "（件名なし）").strip()
    inquiry_id = (record.get("inquiry_id") or "").strip()
    body = (
        f"{STUB_BANNER}\n\n"
        f"{name} 様\n\n"
        f"お問い合わせ「{subject}」（受付番号 {inquiry_id}）を受け付けました。\n"
        "担当者が内容を確認したうえで、改めてご連絡します。\n"
        "このメッセージは下書き見本であり、送信済みではありません。\n"
    )
    return {
        "inquiry_id": inquiry_id,
        "label": STUB_LABEL,
        "synthetic": True,
        "send_status": "not_sent",
        "auto_send": False,
        "queue": "ready_for_review",
        "validation_ok": True,
        "reasons": list(reasons),
        "subject": f"[下書き見本] Re: {subject}",
        "body": body,
    }
