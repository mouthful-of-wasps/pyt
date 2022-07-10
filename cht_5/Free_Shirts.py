    #ecoo19r1p1
for i in range(10):
    sinit = input()

    sinit = sinit.split()

    for i in range(len(sinit)):
        sinit[i] = int(sinit[i])

    # sinit[0] = shirts
    # sinit[1] = no_events
    # sinit[2] = days

    events = input()

    events = events.split()

    for i in range(len(events)):
        events[i] = int(events[i])


    events.sort()


    clean_shirts = sinit[0]
    shirts = clean_shirts
    washes = 0

    for i in range(1,sinit[2]+1):
        if clean_shirts == 0:
            washes += 1
            clean_shirts = shirts
        if i == 1 and events[0] != 1:
            clean_shirts -= 1
        
        else:
            if events and i == events[0]:
                clean_shirts -= 1
                while events and i == events[0]:
                    shirts += 1
                    events.pop(0)
                    clean_shirts += 1
            else:
                clean_shirts -= 1
                


            
            
    print(washes)

        

