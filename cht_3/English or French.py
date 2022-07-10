# ccc11s1

no_lines = int(input())

SSS = 0
TTT = 0



for i in range(no_lines):
    line = input()
    TTT += line.lower().count('t')
    SSS += line.lower().count('s')



if TTT > SSS:
    print('English')
else:
    print('French')

    