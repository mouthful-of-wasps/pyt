# ccc18j2
nos = int(input())
yesterday = input()
today = input()

length = min(len(yesterday),len(today),nos)
equal = 0

for i in range(length):
    if (yesterday[i] == today[i] and today[i] == 'C'):
        equal += 1



print(equal)