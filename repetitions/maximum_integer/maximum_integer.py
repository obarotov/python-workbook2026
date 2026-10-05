import random

max_n = 0
update = 0

for _ in range(100):
    nums = random.randint(1,101)
    print(nums)
    if nums > max_n:
        max_n = nums
        update += 1

print(f"The maximum value found was {max_n}")
print(f"The maximum value was updated {update} times")
