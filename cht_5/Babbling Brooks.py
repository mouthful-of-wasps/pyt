# ccc00s2

nos_streams=int(input())

streams = []

for i in range(nos_streams):
    streams.append(float(input()))


a=0

while a != 77:
    a=int(input())

    if a == 99:
       a = int(input()) 
       part = float(input())
       streams.insert(int(a),(float(streams[a-1])*part/100.0))
       streams[a-1] = streams[a-1] * (1-(part/100.0)) 
       a = 0
    if a == 88:
        a = int(input())
        streams[a]=(float(streams[a]) + float(streams[a-1]))
        del streams[a-1]
        a=0
    


text = f''
for x in range(len(streams)):
   text += f' {int(round(streams[x],0))}'

print(text.strip())