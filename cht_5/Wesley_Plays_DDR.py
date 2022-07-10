#wac3p3

moves = input()

no_of_combos = int(input())

combos = []

for i in range(no_of_combos):
    combos.append(input().split())


#combos = sorted(combos, key=lambda x: len(x[0]), reverse=True)
points = len(moves)


moves_index = 0
while moves_index < len(moves):
    for i in range(len(combos)):
        if combos[i][0] == moves[moves_index:(moves_index+len(combos[i][0]))]:
            points += int(combos[i][1])
            moves_index += (len(combos[i][0]) -1)
            combos.pop(i)
            break
    moves_index+=1

print(points)