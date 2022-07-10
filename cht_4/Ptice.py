nos = int(input())
answers = input()

a = 'ABC'*4
b = 'BABC'*3
g = 'CCAABB'*2

i=0

ppl = {'Adrian':0, 'Bruno':0, 'Goran': 0}

while i < nos:
    index = (i)%12
    svar = answers[i]

    if a[index] == svar:
        ppl['Adrian'] +=1
    if b[index] == svar:
        ppl['Bruno'] +=1
    if g[index] == svar:
        ppl['Goran'] +=1
     
    
    
    i += 1

best_possible = max(ppl.values())

print(best_possible)
for key, value in ppl.items():
    if best_possible == value:
        print(key)