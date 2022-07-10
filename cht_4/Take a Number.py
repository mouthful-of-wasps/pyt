#ecoo13r1p1

#start_no = int(input())

actions = {'TAKE':0,'SERVE':0,'no':int(input())}


while True:
    action = input()
    if len(action) == 3:

        break
    else:
        if action == 'CLOSE':
            print(f'{actions["TAKE"]} {actions["TAKE"]-actions["SERVE"]} {actions["no"]}')
            actions['TAKE'] =0 
            actions['SERVE'] =0
        else: 
            
            if len(action) == 4:
                actions["no"] +=1
                if actions['no'] == 1000:
                    actions['no'] = 1 
                actions['TAKE'] +=1
            elif action == 'SERVE':
                actions['SERVE'] +=1

