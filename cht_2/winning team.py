# ccc19j1
team_a_three_pointers  = int(input())
team_a_two_pointers = int(input())
team_a_one_pointers = int(input())
team_b_three_pointers = int(input())
team_b_two_pointers  = int(input())
team_b_one_pointers  = int(input())

res = (team_a_three_pointers-team_b_three_pointers)*3 + (team_a_two_pointers-team_b_two_pointers)*2 + (team_a_one_pointers-team_b_one_pointers)

if res > 0:
    print('A')
elif res < 0:
     print('B')
else:
    print('T')

