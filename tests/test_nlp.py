import pytest

from src.nlp import clean_text, split_sentences, extract_key_sentences


def test_clean_text_basic():
    s = "  Hello\nworld  "
    assert clean_text(s) == "Hello world"


def test_split_sentences():
    text = "Sales grew 5%. Customer churn decreased. Inventory delayed."
    sents = split_sentences(text)
    assert len(sents) == 3


def test_extract_key_sentences_ordering():
    text = "Sales grew quickly. Random note. Inventory delay caused stockouts. Marketing ROI improved."
    keys = extract_key_sentences(text, top_n=2)
    # expect sentences mentioning growth or inventory to appear
    assert any("sales" in k.lower() or "inventory" in k.lower() for k in keys)
