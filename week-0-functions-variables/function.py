def main():
    name = input("What's your name? ")
    hello(name)

def hello(to: str = "World"):
   return f"Hello, {to}"

main()