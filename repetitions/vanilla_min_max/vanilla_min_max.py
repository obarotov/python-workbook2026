min_value = 0
max_value = 0


while True:
    n = str(input())
    if n == "":
        break
    else:
        n = float("")
        if n > max_value:
            max_value = n

print(max_value)
