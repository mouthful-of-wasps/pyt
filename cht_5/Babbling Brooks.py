# ccc00s2

nos_streams=int(input())

streams = []

for i in range(nos_streams):
    streams.append(float(input()))


input_no=0

while input_no != 77:
    input_no=int(input())

    if input_no == 99:
       input_no = int(input()) 
       part = float(input())
       streams.insert(int(input_no),(float(streams[input_no-1])*part/100.0))
       streams[input_no-1] = streams[input_no-1] * (1-(part/100.0)) 
       input_no = 0
    if input_no == 88:
        input_no = int(input())
        streams[input_no]=(float(streams[input_no]) + float(streams[input_no-1]))
        del streams[input_no-1]
        input_no=0
    


text = f''
for x in range(len(streams)):
   text += f' {int(round(streams[x],0))}'

print(text.strip())