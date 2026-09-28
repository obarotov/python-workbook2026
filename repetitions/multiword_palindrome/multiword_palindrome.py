s = str(input())
s = s.lower()
opposite = ""

for i in range(len(s) -1, -1,-1):
    opposite += s[i]

if opposite == s:
    print(f"`{s}` is a palindrome")
else:
    print(f"`{s}` is not a palindrome")