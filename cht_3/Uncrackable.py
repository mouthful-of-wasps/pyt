# wc17c3j3

# 8-12 Furthermore, it must contain at least three lowercase letters, at least two uppercase letters, and at least one digit.

pw = input()

validation = 'Invalid'
upper = 0
lower = 0
digit = 0

if 8 <= len(pw) <= 12:
 for letter in pw:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif letter.isdigit():
            digit += 1


if (upper > 1 and lower > 2 and digit >0):
    validation = 'Valid'




print(validation)
print(lower)
print(upper)
print(digit)