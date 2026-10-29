"""
Problem: Coke Machine (coke.py)

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only
accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In coke.py, implement a program that prompts the user to insert a coin, one at
a time, each time informing the user of the amount due. Once the user has
inputted at least 50 cents, output how many cents in change the user is owed.

Requirements:
- Repeatedly output "Amount Due: X" and prompt "Insert Coin: " while amount due > 0.
- Assume the user will only input integers.
- Ignore any integer that isn't an accepted denomination (25, 10, or 5).
- Once 50 cents or more have been inserted, output "Change Owed: Y".
"""


def main():
    # TODO: Track the amount due starting at 50 cents
    ...

    # TODO: Loop until the amount due is 0 or less, accepting only 25, 10, or 5 cent coins
    ...

    # TODO: Output the change owed
    ...


if __name__ == "__main__":
    main()

