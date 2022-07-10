#ecoo15r1p1

from typing import no_type_check

nono = 0
colors = {'orange':0,'blue':1,'green':2,'yellow':3,'pink':4,'violet':5, 'brown':6,'red':7}
while nono < 10: 
 anos = (0,0,0,0,0,0,0,0)
 nos = list(anos)


 while True:
     a = input()
     if a == 'end of box':
         break
     else:
        nos[colors[a]] += 1


 time = 0
 index = 0
 for number in nos:
    if number > 0:
        if index != 7:
            time += (13*  (int(number/7) + min(1,number%7)))
        else:
            time += (16* number)
    index +=1



 print(time)
 nono+=1



    