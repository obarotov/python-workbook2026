rows = int(input())
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    up = "".join(str(j) for j in range(1, i + 1))
    down = "".join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + up + down)
