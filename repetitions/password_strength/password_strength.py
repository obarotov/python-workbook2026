password = input()

special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True

criteria_met = 0
if has_upper:
    criteria_met += 1
if has_lower:
    criteria_met += 1
if has_digit:
    criteria_met += 1
if has_special:
    criteria_met += 1
if len(password) >= 8:
    criteria_met += 1

if criteria_met == 5:
    print("Very Strong")
elif criteria_met == 4:
    print("Strong")
elif criteria_met == 3:
    print("Medium")
elif criteria_met == 2:
    print("Weak")
else:
    print("Very Weak")