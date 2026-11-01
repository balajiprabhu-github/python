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
    
    amount_due = 50
    insert_coin = 0
    
    while(amount_due > 0):
        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in (5,10,25):
            amount_due -= insert_coin
    
    print(f"Change Owed: {abs(amount_due)}")
            


if __name__ == "__main__":
    main()

