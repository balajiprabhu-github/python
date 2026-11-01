"""
Problem: Just setting up my twttr (twttr.py)

When texting or tweeting, it's not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr.

In twttr.py, implement a program that prompts the user for a str of text and then
outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether
inputted in uppercase or lowercase.

Requirements:
- Prompt the user with "Input: "
- Omit all vowels (A, E, I, O, U) case-insensitively.
- Output "Output: " followed by the shortened text.
"""


def main():

    text = input("Input: ")
    print("Output: ", end="")

    for char in text:
        if char.lower() not in("a","e","i","o","u"):
            print(char, end="")

    print()

if __name__ == "__main__":
    main()

