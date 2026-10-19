"""
Module 1 Exercises: Syntax, Dynamic Typing, Truthiness, f-strings, Unpacking
=============================================================================
Fill in the TODOs below. Run tests with:
    uv run pytest 01_syntax_types/test_exercises.py
"""

def format_model_metric(model_name: str, latency_ms: float, accuracy: float) -> str:
    """
    Format a model metric string.
    Example:
        format_model_metric("gpt-4o", 124.567, 0.9452)
        -> "[GPT-4O] latency: 124.6ms, accuracy: 94.52%"

    Requirements:
    - Model name in uppercase inside square brackets: [MODEL]
    - Latency formatted to 1 decimal place with 'ms' suffix
    - Accuracy formatted as a percentage with 2 decimal places and '%' suffix
    """
    # TODO: Implement using f-strings
    pass


def safe_token_limit(provided: int | None, default: int = 2048) -> int:
    """
    Return the provided token limit, or `default` if provided is None.

    CRITICAL GOTCHA:
    In Kotlin: `provided ?: default`
    In Python: `provided or default` treats 0 as Falsy, so `0 or 2048` would wrongly return 2048!
    If provided is 0 (e.g. streaming with zero buffering), it must return 0.
    """
    # TODO: Implement handling None vs Falsy
    pass


def split_rag_context(records: list[str]) -> tuple[str, list[str], str]:
    """
    Unpack a sequence of RAG context records:
    - The first record is the system prompt
    - The last record is the user query
    - Everything in between are retrieved document chunks (could be empty list)

    If `records` has fewer than 2 items, raise ValueError("Need at least 2 records").

    Use extended unpacking (*rest).
    """
    # TODO: Implement using extended unpacking
    pass


def merge_llm_kwargs(base: dict, overrides: dict | None = None, **extra) -> dict:
    """
    Merge configuration dictionaries for an LLM call without mutating the inputs.
    Precedence (lowest to highest):
    1. base
    2. overrides (if provided)
    3. extra kwargs

    Example:
        merge_llm_kwargs({"temp": 0.7, "top_p": 1.0}, {"temp": 0.2}, stream=True)
        -> {"temp": 0.2, "top_p": 1.0, "stream": True}
    """
    # TODO: Implement using dictionary unpacking
    pass
