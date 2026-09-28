total = 0

n = str(input())

n_reverse = n[::-1]

for i in range(len(n_reverse)):
    total += int(n_reverse[i]) * 2** i

print(total)
