min_value = float('inf')
max_value = float('-inf')


while True:
    n = str(input())
    if n == "":
        break
    else:
        n = int(n)
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")