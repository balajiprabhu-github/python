"""
Problem: camelCase (camel.py)

In camel.py, implement a program that prompts the user for the name of a variable
in camelCase and outputs the corresponding name in snake_case.

Requirements:
- Prompt the user with "camelCase: "
- Assume that the user's input will indeed be in camelCase.
- Output "snake_case: " followed by the converted variable name.
- Every uppercase letter should be replaced by an underscore (_) followed by its
  lowercase equivalent.
"""


def main():
   
    str = input("camelCase: ")
    print("snake_case: ", end="")
    
    for char in str:
      if(char.isupper()): 
          print("_", end="")
      print(char.lower(), end="")
      
    print()


if __name__ == "__main__":
    main()

