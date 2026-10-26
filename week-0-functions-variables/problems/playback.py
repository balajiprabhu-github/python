def main():
    user_input = input()
    result = convert(user_input)
    print(result)

def convert(text):
    return text.replace(" ","...")

main()