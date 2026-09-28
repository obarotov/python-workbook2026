n = str(input())
binary = ""

if len(n) < 2:
    print(n)
    exit()

while int(n) != 0:
    n = int(n)
    if n % 2 == 0:
        n = n // 2
        binary = '0' + binary
    elif n % 2 != 0:
        n = n // 2
        binary = '1' + binary
print(binary)