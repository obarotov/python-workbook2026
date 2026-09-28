n = str(input())

total = 0
for i in n:
    if i.isdigit():
        i = int(i)
        total += 1
    else:
        continue
print(total)