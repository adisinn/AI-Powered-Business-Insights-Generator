"""NLP helpers and LLM call wrapper.

Includes simple cleaning, sentence splitting, and a keyword-based key-sentence extractor
used as a lightweight alternative to vector/TF-IDF methods for demos.
"""
import os
import re
from typing import List
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def clean_text(text: str) -> str:
    if not text:
        return ""
    # collapse whitespace and normalize
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text: str) -> List[str]:
    """Split text into sentences (naive but robust for short reports)."""
    text = clean_text(text)
    if not text:
        return []
    # split on sentence boundaries while keeping abbreviations simple
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    return sentences


KEYWORDS = [
    "increase",
    "decrease",
    "grew",
    "growth",
    "decline",
    "churn",
    "churned",
    "satisf",
    "delay",
    "inventory",
    "roi",
    "marketing",
    "launch",
    "refund",
    "dipped",
    "improved",
]


def extract_key_sentences(text: str, top_n: int = 5) -> List[str]:
    """Return the top_n sentences scored by keyword presence and length heuristics.

    This is intentionally lightweight for offline demos and interview settings.
    """
    sentences = split_sentences(text)
    if not sentences:
        return []

    scored = []
    for s in sentences:
        s_lower = s.lower()
        # score by keyword hits
        kw_score = sum(1 for kw in KEYWORDS if kw in s_lower)
        # small length boost so very short sentences are deprioritized
        length_score = min(len(s) / 200.0, 1.0)
        score = kw_score + length_score
        scored.append((score, s))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [s for _, s in scored[:top_n]]


def call_llm(prompt: str, max_tokens: int = 1000) -> str:
    """Call Groq LLM using native Groq SDK with llama-3.3-70b model.

    Groq provides fast inference with Llama 3.3 70B model.
    """
    try:
        from groq import Groq
    except Exception:
        return "[Groq library not installed: run 'pip install groq']"

    if not GROQ_API_KEY:
        return "[GROQ_API_KEY not set — set it in your environment to enable LLM calls]"

    try:
        client = Groq(api_key=GROQ_API_KEY)
        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=max_tokens,
        )
        text = resp.choices[0].message.content.strip()
        return text
    except Exception as e:
        # Return detailed error for debugging
        error_msg = str(e)
        print(f"[DEBUG] Groq API Error: {error_msg}")
        return f"[Groq API Error: {error_msg[:100]}]"
