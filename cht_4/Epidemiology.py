#ccc20j2

target = int(input())
day_zero = int(input())
multiple = int(input())
day = 0

target = target - day_zero
while target >= 0:
    if multiple == 1:
        target = target + day_zero
        day = (round((target - (target % day_zero)) / day_zero))
        break
    else:
        day +=1
        day_zero = day_zero*multiple
        target = target - day_zero


print(day)