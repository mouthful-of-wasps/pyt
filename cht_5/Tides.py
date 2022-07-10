#dmopc14c7p2i
no_readings = int(input())

readings = input()
readings = readings.split()

for i in range(len(readings)):
    readings[i] = int(readings[i])

index_max = max(range(len(readings)), key=readings.__getitem__)
index_min = min(range(len(readings)), key=readings.__getitem__)

readings = readings[index_min:index_max+1]


r2 = readings.copy()
readings.sort()
if r2 == readings and index_min < index_max:
    print(readings[-1]-readings[0])
else:
    print(f'unknown')
   