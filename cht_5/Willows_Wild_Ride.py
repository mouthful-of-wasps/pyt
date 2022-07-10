    #ecoo18r1p1
for i in range(10):
    boxe_dage = input()

    boxe_dage = boxe_dage.split()

    for i in range(len(boxe_dage)):
        boxe_dage[i] = int(boxe_dage[i])


    boxes = 0
    dage_brugt = 0

    for i in range(boxe_dage[1]):
        i_dag = input()

        if i_dag == 'E':
            if boxes>0:
                dage_brugt += 1
                if dage_brugt == boxe_dage[0]:
                    boxes -= 1
                    dage_brugt = 0
        else:
            boxes += 1
            dage_brugt += 1
            if dage_brugt == boxe_dage[0]:
                    boxes -= 1
                    dage_brugt = 0
        
                    
                    
                    
                    
    resterende_dage = ((boxes-1) * boxe_dage[0]) + (boxe_dage[0] - dage_brugt)

    print(resterende_dage)


