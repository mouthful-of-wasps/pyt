the_string = input()


ball_place = '1'


for move in the_string:
    if move + ball_place == 'A1':
        ball_place = '2'
    elif move + ball_place == 'A2':
        ball_place = '1'
    elif move + ball_place == 'A3':
        ball_place = '3'
    elif move + ball_place == 'B1':
        ball_place = '1' 
    elif move + ball_place == 'B2':
        ball_place = '3' 
    elif move + ball_place == 'B3':
        ball_place = '2' 
    elif move + ball_place == 'C1':
        ball_place = '3' 
    elif move + ball_place == 'C2':
        ball_place = '2' 
    elif move + ball_place == 'C3':
        ball_place = '1' 



print(ball_place)
    