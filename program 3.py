a=int(input("INPUT :"))
def print_pattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print(chr(65 + j), end="")
        for j in range(i, 0, -1):
            print(chr(64 + j), end="")
        print()
print_pattern(6)
