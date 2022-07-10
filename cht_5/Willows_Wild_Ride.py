    #ecoo18r1p1
for i in range(10):
    box_days = input()

    box_days = box_days.split()

    for i in range(len(box_days)):
        box_days[i] = int(box_days[i])


    boxes = 0
    days_gone = 0

    for i in range(box_days[1]):
        today = input()

        if today == 'E':
            if boxes>0:
                days_gone += 1
                if days_gone == box_days[0]:
                    boxes -= 1
                    days_gone = 0
        else:
            boxes += 1
            days_gone += 1
            if days_gone == box_days[0]:
                    boxes -= 1
                    days_gone = 0
        
                    
                    
                    
                    
    days_left = ((boxes-1) * box_days[0]) + (box_days[0] - days_gone)

    print(days_left)


