parity_even = 0
parity_odd = 0

while True:
    nums = input()

    if nums == "":
        break
    else:
        nums = str(nums)
        if len(nums) < 8:
            print("Error: Input must be exactly 8 bits")
            break
        else:
            for i in nums:
                if int(i) == 0:
                    parity_even += 1
                elif int(i) == 1:
                    parity_odd += 1
    print(f"Parity bit: {0 if parity_even % 2 == 0 else 1}")