"""Prompt templates and examples for demo/interview use."""

SIMPLE_INSIGHT_TEMPLATE = (
    "You are a senior business analyst. Given the following key report excerpts, produce:\n"
    "- 3 concise actionable insights (one sentence each)\n"
    "- For each insight, provide a short explanation and a suggested metric to track\n\n"
    "Report excerpts:\n{excerpts}\n\n"
    "Data summary:\n{data_summary}\n\n"
    "Output format:\n1) Insight: ...\n   Explanation: ...\n   Metric: ...\n2) ...\n3) ...\n"
)

EXAMPLE_PROMPTS = {
    "growth_focus": {
        "desc": "Ask the LLM to prioritize growth opportunities and channel allocation.",
        "prompt": (
            "Given the excerpts below, identify the top 2 channels to scale, risks, and a quick test to validate scaling:\n\n{excerpts}"
        ),
    },
    "retention_focus": {
        "desc": "Ask the LLM to focus on retention strategies and root-cause hypotheses.",
        "prompt": (
            "Review the following and provide 3 root-cause hypotheses for churn and 3 short tests we can run to validate them:\n\n{excerpts}"
        ),
    },
}
