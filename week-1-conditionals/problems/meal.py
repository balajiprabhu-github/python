"""
Problem: Meal Time (meal.py)

In meal.py, implement a program that prompts the user for a time and outputs whether
it’s breakfast time, lunch time, or dinner time.

Requirements:
- Breakfast: 7:00 to 8:00 (inclusive)   -> "breakfast time"
- Lunch:    12:00 to 13:00 (inclusive)  -> "lunch time"
- Dinner:   18:00 to 19:00 (inclusive)  -> "dinner time"
- If it's not time for a meal, output nothing at all.
- Structure:
    - Implement convert(time): converts a str in 24-hr format (e.g. "7:30")
      to a corresponding float (e.g. 7.5).
    - Call convert inside main() to decide what to print.
"""

def main():
    user_input = input("What time is it? ")

    result = convert(user_input)

    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    return float(hour) + float(minute) / 60
    

if __name__ == "__main__":
    main()
