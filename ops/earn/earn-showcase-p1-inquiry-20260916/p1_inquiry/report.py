"""HTML and text reports for the hold-for-human queues."""

from __future__ import annotations

from html import escape
from typing import Any


def render_html(result: dict[str, Any]) -> str:
    summary = result["summary"]
    records = result["records"]
    ready = result["ready_for_review"]
    hold = result["needs_human"]

    def rows(items: list[dict], extra: str = "") -> str:
        if not items:
            return '<tr><td colspan="6" class="empty">該当なし</td></tr>'
        out = []
        for item in items:
            out.append(
                "<tr>"
                f"<td>{escape(item['inquiry_id'])}</td>"
                f"<td>{escape(item['received_at'])}</td>"
                f"<td>{escape(item['name'])}</td>"
                f"<td>{escape(item['subject'])}</td>"
                f"<td>{escape(item['queue'])}</td>"
                f"<td>{escape(item['reason_text'])}</td>"
                "</tr>"
            )
        return "\n".join(out)

    input_rows = []
    for item in records:
        input_rows.append(
            "<tr>"
            f"<td>{escape(item['inquiry_id'])}</td>"
            f"<td>{escape(item['channel'])}</td>"
            f"<td>{escape(item['name'])}</td>"
            f"<td>{escape(item['email'] or '—')}</td>"
            f"<td>{escape(item['phone'] or '—')}</td>"
            f"<td>{escape(item['subject'])}</td>"
            "</tr>"
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>P1 問い合わせ受付見本（合成）</title>
  <style>
    :root {{
      --ink: #1b2430;
      --muted: #5c6b7a;
      --paper: #f4efe6;
      --card: #fffdf8;
      --line: #d7cfc2;
      --hold: #8a3b12;
      --hold-bg: #f4ddcf;
      --review: #1f4d43;
      --review-bg: #d7ebe4;
      --stamp: #9b1d2a;
    }}
    body {{
      margin: 0;
      font-family: "Noto Sans CJK JP", "Noto Sans JP", "Hiragino Sans", sans-serif;
      background: var(--paper);
      color: var(--ink);
    }}
    header, section, footer {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 24px 20px;
    }}
    header {{
      border-bottom: 4px solid var(--ink);
    }}
    .stamp {{
      display: inline-block;
      border: 3px solid var(--stamp);
      color: var(--stamp);
      font-weight: 700;
      letter-spacing: 0.12em;
      padding: 4px 10px;
      transform: rotate(-6deg);
    }}
    h1 {{ margin: 12px 0 8px; font-size: 28px; }}
    p.lead {{ color: var(--muted); }}
    .kpis {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin: 16px 0 0;
    }}
    .kpi {{
      background: var(--card);
      border: 1px solid var(--line);
      padding: 12px;
    }}
    .kpi b {{ display: block; font-size: 28px; }}
    .kpi span {{ color: var(--muted); font-size: 12px; }}
    note, .note {{
      display: block;
      margin-top: 10px;
      color: var(--muted);
      font-size: 13px;
    }}
    section {{
      background: var(--card);
      border: 1px solid var(--line);
      margin: 18px auto;
    }}
    h2 {{ margin-top: 0; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    th, td {{
      border-bottom: 1px solid var(--line);
      text-align: left;
      padding: 8px 6px;
      vertical-align: top;
      overflow-wrap: anywhere;
    }}
    th {{ color: var(--muted); font-weight: 600; }}
    .hold {{ background: var(--hold-bg); }}
    .review {{ background: var(--review-bg); }}
    footer {{ color: var(--muted); font-size: 12px; }}
  </style>
</head>
<body>
  <header id="screen-input">
    <div class="stamp">SYNTHETIC / 合成</div>
    <h1>問い合わせ受付見本 P1</h1>
    <p class="lead">入力検査 → 重複判定 → 人が止める確認待ち一覧。送信・公開・登録はしません。</p>
    <div class="kpis">
      <div class="kpi"><span>入力件数（このfixture）</span><b>{summary["input_count"]}</b></div>
      <div class="kpi review"><span>整理済み・人の確認待ち</span><b>{summary["ready_for_review"]}</b></div>
      <div class="kpi hold"><span>要確認（閉じて止める）</span><b>{summary["needs_human"]}</b></div>
      <div class="kpi"><span>送信 / 公開</span><b>{summary["sent"]} / {summary["published"]}</b></div>
    </div>
    <p class="note">{escape(summary["disclaimer"])}</p>
  </header>

  <section id="screen-intake">
    <h2>画面1. 受付入力（合成20件）</h2>
    <p>連絡先はすべて example.com / 架空番号。実在の個人情報ではありません。</p>
    <table>
      <thead><tr><th>ID</th><th>経路</th><th>名前</th><th>メール</th><th>電話</th><th>件名</th></tr></thead>
      <tbody>
        {''.join(input_rows)}
      </tbody>
    </table>
  </section>

  <section id="screen-validation">
    <h2>画面2. 入力検査と重複判定</h2>
    <p>曖昧・欠損・将来日付・リスク語・同一連絡先はすべて needs_human。自動で通さない。</p>
    <table>
      <thead><tr><th>ID</th><th>受信</th><th>名前</th><th>件名</th><th>キュー</th><th>理由</th></tr></thead>
      <tbody>
        {rows(records)}
      </tbody>
    </table>
  </section>

  <section id="screen-hold">
    <h2>画面3. 確認待ち一覧</h2>
    <h3 class="hold">要確認（{len(hold)}）— 閉じて止める</h3>
    <table>
      <thead><tr><th>ID</th><th>受信</th><th>名前</th><th>件名</th><th>キュー</th><th>理由</th></tr></thead>
      <tbody>
        {rows(hold)}
      </tbody>
    </table>
    <h3 class="review">整理済み（{len(ready)}）— 返信してよいのは人の承認後だけ</h3>
    <table>
      <thead><tr><th>ID</th><th>受信</th><th>名前</th><th>件名</th><th>キュー</th><th>理由</th></tr></thead>
      <tbody>
        {rows(ready)}
      </tbody>
    </table>
  </section>

  <footer>
    {escape(summary["ticket"])} / {escape(summary["dataset"])} / sent=0 published=0 secrets=0
  </footer>
</body>
</html>
"""


def render_facts_stamp(result: dict[str, Any]) -> str:
    s = result["summary"]
    return (
        "SYNTHETIC / SELF-MADE / NOT A CUSTOMER RESULT\n"
        f"ticket={s['ticket']}\n"
        f"dataset={s['dataset']}\n"
        f"input_count={s['input_count']}\n"
        f"ready_for_review={s['ready_for_review']}\n"
        f"needs_human={s['needs_human']}\n"
        f"sent={s['sent']}\n"
        f"published={s['published']}\n"
        f"secrets_used={s['secrets_used']}\n"
        f"{s['disclaimer']}\n"
    )
