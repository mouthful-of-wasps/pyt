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

previous_score = 'a' if a[0] < b[0] else "b"

if previous_score == 'a':
    a_score += 1
    del a[0]
else:
    b_score +=1
    del b[0]

def who_is_ahead(a_score,b_score, current_,score_before_last_change):
    global previous_score
    global current
    previous_score = score_before_last_change
    current = current_
    if a_score > b_score:
        if previous_score == 'b':
            current+=1
            previous_score = 'a'
            return
    elif a_score < b_score:
        if previous_score == 'a':
            current+=1
            previous_score = 'b'
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
    who_is_ahead(a_score,b_score,current,previous_score)
    

while len(a) > 0:
     #   print(f'a , a:{a_score} - b {b_score}')
        a_score += 1
        who_is_ahead(a_score,b_score,current,previous_score)
        del a[0]
        

while len(b) > 0:
      #  print(f'b , a:{a_score} - b {b_score}')
        b_score += 1
        who_is_ahead(a_score,b_score,current,previous_score)
        del b[0]









print(points_first_half)
print(current)