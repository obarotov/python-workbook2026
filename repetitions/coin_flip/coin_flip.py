import random

total_flips = 0

for _ in range(10):
    flips = ""
    
    while True:
        flips += random.choice(["H", "T"])
        if flips.endswith("HHH") or flips.endswith("TTT"):
            break
            
    count = len(flips)
    total_flips += count
    
    spaced_flips = " ".join(flips)
    print(f"{spaced_flips} ({count} flips)")

print(f"On average, {total_flips / 10:.1f} flips were needed.")
