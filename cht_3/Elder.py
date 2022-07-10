#coci18c4p1
# 
starter = str(input())

fights = int(input())

nos = starter

for i in range(fights):
    fight = input()

    if fight[-1] == starter:
  
        starter = fight[0]
        nos = nos + fight[0]
        



print(starter)
print(len(set(nos)))