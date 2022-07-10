from itertools import count

string_in = input()


happy = string_in.count(':-)')
sad = string_in.count(':-(')

if happy == sad:
    if happy == 0:
        print('none')
    else:
        print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')
