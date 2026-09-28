message = input()
shift = int(input())

result = []

for char in message:
    if char.isalpha():
        if char.isupper():
            base = ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
    else:
        result.append(char)

print("".join(result))