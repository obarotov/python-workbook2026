max_streak = 0
best = 0

while True:
    n = input()
    if n == "":
        break

    n = int(n)
    if n == 1:
        max_streak += 1
        if max_streak > best:
            best = max_streak

    elif n == 0:
        max_streak = 0

print(f"Maximum streak: {best}")
