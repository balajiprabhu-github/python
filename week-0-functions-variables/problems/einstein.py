def main():
    m = int(input("Enter mass: "))
    result = findE(m)
    print(result)

def findE(m):
    c = 300000000
    return m * (c * c)

main()