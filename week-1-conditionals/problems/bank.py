"""
Problem: Home Federal Savings Bank (bank.py)

In bank.py, implement a program that prompts the user for a greeting.

Requirements:
- If the greeting starts with "hello", output: $0
- If the greeting starts with an "h" (but not "hello"), output: $20
- Otherwise, output: $100
- Ignore any leading whitespace and treat the greeting case-insensitively.
"""

def main():
   
    user_input = input("Greeting: ")
    
    greeting = user_input.strip().lower()
    
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
