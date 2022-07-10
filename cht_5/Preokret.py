#coci18c2p1


a_points = int(input())
a = []
b = []
for i in range(a_points):
    a.append(int(input()))

b_points = int(input())

for i in range(b_points):
    b.append(int(input()))


points_first_half = len([1 for i in a if i <= 1440]) + len([1 for i in b if i <= 1440])

current = 0
a_score = 0
b_score = 0

tidligere_stilling = 'a' if a[0] < b[0] else "b"

if tidligere_stilling == 'a':
    a_score += 1
    del a[0]
else:
    b_score +=1
    del b[0]

def hvem_ahead(a_score,b_score, current_,tidligere_stilling_):
    global tidligere_stilling
    global current
    tidligere_stilling = tidligere_stilling_
    current = current_
    if a_score > b_score:
        if tidligere_stilling == 'b':
            current+=1
            tidligere_stilling = 'a'
            return
    elif a_score < b_score:
        if tidligere_stilling == 'a':
            current+=1
            tidligere_stilling = 'b'
            return
    else:
        return





while len(a) > 0 and len(b) > 0:
  #  print(f'tidligere {tidligere_stilling}, a:{a_score} - b {b_score}')
    if a[0] < b[0]:
        a_score +=1
        
        del a[0]
    else:
        b_score +=1
        del b[0]
    hvem_ahead(a_score,b_score,current,tidligere_stilling)
    

while len(a) > 0:
     #   print(f'a , a:{a_score} - b {b_score}')
        a_score += 1
        hvem_ahead(a_score,b_score,current,tidligere_stilling)
        del a[0]
        

while len(b) > 0:
      #  print(f'b , a:{a_score} - b {b_score}')
        b_score += 1
        hvem_ahead(a_score,b_score,current,tidligere_stilling)
        del b[0]









print(points_first_half)
print(current)