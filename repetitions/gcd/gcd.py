max_divisor = 0

num1 = int(input())
num2 = int(input())

for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        max_divisor = i
    elif num1 % i == 0 != num2 % i == 0:
        break
print(max_divisor)