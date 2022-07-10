songs = 'ABCDE'

button = 0

while button != 4:
    
    button = int(input())
    nos = int(input())
    for tal in range(nos):
        the_real_button = button%4

        if the_real_button ==1:
            songs = songs[1:] + songs[0]
        elif the_real_button ==2:
            songs = songs[4] + songs[:4]
        elif the_real_button==3:
            songs = songs[1] + songs[0] + songs[2:]


print(f'{songs[0]} {songs[1]} {songs[2]} {songs[3]} {songs[4]}')
