"""
Problem: Math Interpreter (interpreter.py)

In interpreter.py, implement a program that prompts the user for an arithmetic expression
and then calculates and outputs the result as a floating-point value formatted to
one decimal place (e.g. 2.0).

Requirements:
- Assume the user's input is formatted as: `x y z`, separated by a single space.
- `x` is an integer
- `y` is an operator: `+`, `-`, `*`, or `/`
- `z` is an integer
- Output formatted to 1 decimal place (e.g. f"{result:.1f}")
"""

def main():
    
    user_input = input("Expression: ")

    x, y, z = user_input.strip().split(" ")

    result = calculate(x, z, y)
    
    print(f"{result:.1f}")

def calculate(x: str, z: str, operator: str):
    if operator == "+":
        return float(x) + float(z)
    elif operator == "-":
        return float(x) - float(z)
    elif operator == "*":
        return float(x) * float(z)
    elif operator == "/":
        return float(x) / float(z)


if __name__ == "__main__":
    main()
