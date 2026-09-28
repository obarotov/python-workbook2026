start = float(input())
ratio = float(input())
count = int(input())

current = start
for _ in range(count):
    if current.is_integer():
        print(int(current))
    else:
        print(current)
    current *= ratio