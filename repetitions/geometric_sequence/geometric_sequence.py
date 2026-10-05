start = float(input())
ratio = float(input())
count = int(input())


for seq in range(count):
    res = start * seq * ratio
    print(res)
