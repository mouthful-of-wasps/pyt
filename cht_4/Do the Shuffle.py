songs = 'ABCDE'

button = 0

while button != 4:
    
    button = int(input())
    nos = int(input())
    for tal in range(nos):
        knappen = button%4

        if knappen ==1:
            songs = songs[1:] + songs[0]
        elif knappen ==2:
            songs = songs[4] + songs[:4]
        elif knappen==3:
            songs = songs[1] + songs[0] + songs[2:]


print(f'{songs[0]} {songs[1]} {songs[2]} {songs[3]} {songs[4]}')
