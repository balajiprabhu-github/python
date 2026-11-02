"""
Problem: Nutrition Facts (nutrition.py)

The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters
that "show nutrition information for the 20 most frequently consumed raw fruits
... in the United States."

In nutrition.py, implement a program that prompts consumers users to input a
fruit (case-insensitively) and then outputs the number of calories in one
portion of that fruit, per the FDA's poster for fruits.

Requirements:
- Prompt the user with "Item: "
- Treat input case-insensitively.
- If the input is one of the 20 FDA raw fruits, output "Calories: X".
- Ignore any input that isn't a fruit in the list (output nothing).

FDA Raw Fruits & Calories:
- Apple: 130             - Kiwifruit: 90          - Pear: 100
- Avocado: 50            - Lemon: 15              - Pineapple: 50
- Banana: 110            - Lime: 20               - Plums: 70
- Cantaloupe: 50         - Nectarine: 60          - Strawberries: 50
- Grapefruit: 60         - Orange: 80             - Sweet Cherries: 100
- Grapes: 90             - Peach: 60              - Tangerine: 50
- Honeydew Melon: 50     - Watermelon: 80
"""


def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    fruit = input("Item: ")

    if fruit.lower() in fruits :
        print(f"Calories: {fruits.get(fruit.lower())}")


if __name__ == "__main__":
    main()

