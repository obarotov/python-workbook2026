total = 0

while True:
    n = input()
    if n == "":
        break

    n = int(n)

    if n <= 2:
        total += 0
    elif 3 <= n <= 12:
        total += 14
    elif n >= 65:
        total += 18
    else:
        total += 23

print(f"${total:.2f}")
