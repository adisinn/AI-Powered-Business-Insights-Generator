from src.insights import build_prompt, _fallback_generate_insights


def test_build_prompt_contains_excerpts():
    text = "Sales grew 10%. Customer satisfaction dipped."
    prompt = build_prompt(text, top_n=2)
    assert "Report excerpts" in prompt or "Report excerpts:" in prompt


def test_fallback_generates_three_insights():
    text = "Sales grew; churn increased; inventory delays caused issues."
    out = _fallback_generate_insights(text)
    # fallback returns multiple numbered insights
    assert "1) Insight:" in out
