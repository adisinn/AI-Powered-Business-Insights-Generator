# Prompt Templates & Examples

This file lists useful prompt templates and example prompts you can use during interviews or demos.

- **Simple insight template**: Use `src/prompt_templates.SIMPLE_INSIGHT_TEMPLATE` to provide excerpts and optional data summary. This produces 3 concise actionable insights with metrics.

- **Growth-focused prompt**: Prioritize channels and scaling ideas. Example usage:

```
{excerpts}

Given the excerpts above, identify top 2 channels to scale, risks, and a quick test to validate scaling.
```

- **Retention-focused prompt**: Ask for root-cause hypotheses and validation tests.

```
{excerpts}

Provide 3 root-cause hypotheses for churn and 3 short tests to validate them.
```

Tips:
- Keep excerpts to the most relevant sentences; use `top_n=5` for short reports and increase for longer documents.
- When asking the LLM for metrics, be explicit about time windows (e.g., "monthly churn rate").
