"""Insight generation: build prompts and format LLM responses."""
from typing import Optional
from .nlp import extract_key_sentences, call_llm


def build_prompt(report_text: str, top_n: int = 5, data_summary: Optional[str] = None) -> str:
    key_sentences = '\n'.join(extract_key_sentences(report_text, top_n=top_n))
    prompt = (
        "You are a helpful business analyst. Given the following key report excerpts, produce:\n"
        "- 3 concise actionable insights (one sentence each)\n"
        "- For each insight, provide a short explanation and a suggested metric to track\n\n"
        "Report excerpts:\n"
        + key_sentences
    )
    if data_summary:
        prompt += "\n\nData summary:\n" + data_summary
    prompt += (
        "\n\nOutput format:\n1) Insight: ...\n   Explanation: ...\n   Metric: ...\n2) ...\n3) ...\n"
    )
    return prompt


def _fallback_generate_insights(report_text: str) -> str:
    """Create simple rule-based insights when LLMs are not available (demo fallback)."""
    sents = extract_key_sentences(report_text, top_n=8)
    joined = ' '.join(sents).lower()
    insights = []
    if any(k in joined for k in ["grew", "growth", "increase", "improved"]):
        insights.append(("Sales momentum detected: prioritize scaling top channels.",
                         "Recent growth driven by specific channels; double down on high-ROI campaigns.",
                         "Channel-wise revenue, conversion rate"))
    if any(k in joined for k in ["churn", "refund", "dipped"]):
        insights.append(("Customer experience risk: investigate churn drivers.",
                         "Mentions of churn/refunds point to product or delivery issues affecting retention.",
                         "Churn rate, NPS, refund rate"))
    if any(k in joined for k in ["inventory", "delay"]):
        insights.append(("Supply chain friction: optimize inventory and supplier SLAs.",
                         "Inventory turnover slowed due to delays — could hurt availability and sales.",
                         "Inventory turnover, stockouts"))
    if not insights:
        # generic fallback
        insights = [
            ("Make customer retention a priority.", "Review recent service issues and refunds.", "Churn rate"),
            ("Monitor marketing ROI closely.", "Track cost-per-conversion by channel.", "CPC, CAC, ROAS"),
            ("Keep close watch on inventory.", "Prevent stockouts by improving supplier lead times.", "Inventory turnover"),
        ]

    out_lines = []
    for i, (ins, expl, metric) in enumerate(insights[:3], start=1):
        out_lines.append(f"{i}) Insight: {ins}\n   Explanation: {expl}\n   Metric: {metric}")
    return "\n\n".join(out_lines)


def generate_insights(report_text: str, data_summary: Optional[str] = None, top_n: int = 5) -> str:
    prompt = build_prompt(report_text, top_n=top_n, data_summary=data_summary)
    llm_out = call_llm(prompt)
    # detect LLM-unavailable messages and fall back
    if llm_out.startswith("["):
        return _fallback_generate_insights(report_text)
    return llm_out
