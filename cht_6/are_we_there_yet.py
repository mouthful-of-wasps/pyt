#DMOJ problem ccc18j3, Are we there yet?

def test(dis = input()):

    dis = dis.split(' ')

    dis = list(map(int,dis))

    town = 0

    while town < 5:
        dis.insert(town,0)
        #print(dis[town:4])

        last = sum(dis[town:5]) 
        secondtolast = sum(dis[town:4]) if town < 3 else 0 if town==3 else sum(dis[3:town+1])
        middle =  sum(dis[town:3]) if town < 2 else  0 if town==2 else sum(dis[2:town+1]) 
        second = sum(dis[town:2]) if town < 1 else 0 if town==1 else sum(dis[1:town+1])  
        first = 0 if town == 0 else sum(dis[0:town+1])

        print(f'{first} {second} {middle} {secondtolast} {last}')


        del(dis[town])
        town +=1




test()


