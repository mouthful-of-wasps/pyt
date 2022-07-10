# coci13c3p1

tryk = int(input())

streng = 'A'

A = 1
B = 1

if tryk < 1:
    print('1 0')
elif tryk == 1:
    print('0 1')
else:
    for i in range(tryk-2):
        C = B
        B += A
        A = C
    
    print(str(A) + ' ' + str(B))