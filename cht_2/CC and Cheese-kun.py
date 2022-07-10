units = int(input())
cheese = int(input())


if units == 3 and cheese >= 95:
    how = 'absolutely'
elif units == 1 and cheese <= 50:
    how = 'fairly'
else:
    how = 'very'

print('C.C. is ' + how + ' satisfied with her pizza.')