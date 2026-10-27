"""
Problem: Deep Thought (deep.py)

In deep.py, implement a program that prompts the user for the answer to the
Great Question of Life, the Universe and Everything.

Requirements:
- Output 'Yes' if the user inputs:
    - 42
    - forty-two (case-insensitively)
    - forty two (case-insensitively)
- Output 'No' otherwise.
- Remember to handle leading/trailing whitespace and case-insensitivity.
"""

def main():
    
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    cleaned_input = user_input.strip().lower()
    if cleaned_input in ("42", "forty-two", "forty two"):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
