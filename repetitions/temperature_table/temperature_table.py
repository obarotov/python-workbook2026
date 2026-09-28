print(f"{"Celsius":>2} {"Fahrenheit":>10}")
for i in range(0, 101, 10):
    print(f"{i:>2} {i * 9/5 + 32:>10}")