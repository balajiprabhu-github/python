"""
Module 1: Syntax, Dynamic Typing, Truthiness, f-strings, Unpacking
==================================================================
Kotlin vs Python comparison for Android engineers.
"""

def demo_dynamic_typing_and_identity():
    # In Kotlin: static typing with strong compile-time guarantees (val / var).
    # In Python: variables are untyped names bound to typed objects.
    x = 42
    print(f"Type of x: {type(x)}, id: {id(x)}")
    x = "Now I am a string"
    print(f"Type of x: {type(x)}, id: {id(x)}")

    # `is` vs `==`:
    # `==` checks structural equality (like Kotlin `==`)
    # `is` checks referential identity (like Kotlin `===`)
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(f"a == b: {a == b}")  # True (same values)
    print(f"a is b: {a is b}")  # False (distinct objects in memory)


def demo_none_and_truthiness():
    # 1. Null handling:
    # Kotlin: val name: String? = null
    # Python: name = None
    # Idiomatic check: always use `is None` or `is not None` (never `== None`)
    user: str | None = None
    if user is None:
        print("User is not provided")

    # 2. Elvis operator equivalent:
    # Kotlin: user ?: "Guest"
    # Python: user or "Guest"  (CAREFUL: checks truthiness, not just None!)
    # If user is "" (empty string), `user or "Guest"` yields "Guest" because "" is falsy!
    name = ""
    fallback_truthy = name or "Guest"  # Yields "Guest"
    fallback_none_only = name if name is not None else "Guest"  # Yields ""
    print(f"Truthy fallback: '{fallback_truthy}', None-only fallback: '{fallback_none_only}'")

    # 3. Truthiness:
    # In Kotlin, `if (x)` strictly requires a Boolean.
    # In Python, any empty collection or zero-like value is Falsy:
    #   Falsy: None, False, 0, 0.0, "", [], {}, set(), ()
    #   Truthy: everything else
    items = []
    if not items:
        print("items list is empty (no items.isEmpty() needed!)")


def demo_fstrings():
    # Like Kotlin string templates "$name" or "${user.age}"
    model = "gpt-4o"
    tokens = 1520
    cost_per_1k = 0.005
    total_cost = (tokens / 1000) * cost_per_1k

    # Formatting specifiers:
    # :.2f -> 2 decimal float
    # :,   -> thousands separator
    # :>10 -> right-aligned with width 10
    print(f"Model: {model:<10} | Tokens: {tokens:,} | Cost: ${total_cost:.4f}")

    # Self-documenting expressions (added in Python 3.8):
    score = 0.9856
    print(f"{score=:.2%}")  # Prints: score=98.56%


def demo_unpacking():
    # 1. Tuple / List unpacking (destructuring)
    point = (10, 20)
    x, y = point

    # 2. Swapping variables without a temporary variable
    x, y = y, x
    print(f"Swapped: x={x}, y={y}")

    # 3. Extended / Starred unpacking (*rest):
    # Like Kotlin/JavaScript spread operator, but directly in assignment
    values = [1, 2, 3, 4, 5, 6]
    first, *middle, last = values
    print(f"First: {first}, Middle: {middle}, Last: {last}")

    # 4. Dictionary unpacking:
    base_config = {"temperature": 0.7, "max_tokens": 1000}
    custom_config = {**base_config, "temperature": 0.2, "top_p": 0.95}
    print(f"Merged config: {custom_config}")


if __name__ == "__main__":
    print("--- Dynamic Typing & Identity ---")
    demo_dynamic_typing_and_identity()
    print("\n--- None & Truthiness ---")
    demo_none_and_truthiness()
    print("\n--- f-strings ---")
    demo_fstrings()
    print("\n--- Unpacking ---")
    demo_unpacking()
