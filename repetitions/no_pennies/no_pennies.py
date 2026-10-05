total = 0

while True:
    a = input()
    if a == "":
        break
    a = float(a)
    total += a

print(f"Total: ${total:.2f}")
print(f"Cash payment: ${round(total / 0.05 ) * 0.05:.2f}")
