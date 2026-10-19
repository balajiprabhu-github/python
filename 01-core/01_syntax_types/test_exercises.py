import pytest
from exercises import (
    format_model_metric,
    safe_token_limit,
    split_rag_context,
    merge_llm_kwargs,
)

def test_format_model_metric():
    res = format_model_metric("gpt-4o", 124.567, 0.9452)
    assert res == "[GPT-4O] latency: 124.6ms, accuracy: 94.52%"

    res2 = format_model_metric("claude-3-5-sonnet", 45.0, 1.0)
    assert res2 == "[CLAUDE-3-5-SONNET] latency: 45.0ms, accuracy: 100.00%"


def test_safe_token_limit():
    assert safe_token_limit(4096) == 4096
    assert safe_token_limit(None) == 2048
    assert safe_token_limit(None, default=1024) == 1024
    # Critical edge case: 0 is falsy, but valid int!
    assert safe_token_limit(0) == 0


def test_split_rag_context():
    records = ["You are a helpful AI", "doc chunk 1", "doc chunk 2", "What is RAG?"]
    sys_prompt, docs, query = split_rag_context(records)
    assert sys_prompt == "You are a helpful AI"
    assert docs == ["doc chunk 1", "doc chunk 2"]
    assert query == "What is RAG?"

    # Two elements (empty docs)
    sys_prompt, docs, query = split_rag_context(["System", "User query"])
    assert sys_prompt == "System"
    assert docs == []
    assert query == "User query"

    # Fewer than 2 elements should raise ValueError
    with pytest.raises(ValueError, match="Need at least 2 records"):
        split_rag_context(["Only system"])

    with pytest.raises(ValueError, match="Need at least 2 records"):
        split_rag_context([])


def test_merge_llm_kwargs():
    base = {"temperature": 0.7, "max_tokens": 1000}
    overrides = {"temperature": 0.2}

    merged = merge_llm_kwargs(base, overrides, stream=True, user_id="user_123")

    assert merged == {
        "temperature": 0.2,
        "max_tokens": 1000,
        "stream": True,
        "user_id": "user_123",
    }
    # Ensure immutability (original base was not modified)
    assert base == {"temperature": 0.7, "max_tokens": 1000}

    # Handling overrides=None
    merged_none = merge_llm_kwargs(base, None, max_tokens=2000)
    assert merged_none == {"temperature": 0.7, "max_tokens": 2000}
