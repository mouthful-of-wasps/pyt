#ecoo17r3p1

for ii in range(10):

    indtast = input().split()

    shops=int(indtast[0])
    days=int(indtast[1])

    grid = []
    for i in range(days):
        row=input().split()
        for j in range(shops):
            row[j]=int(row[j])
        grid.append(row)
    
    bonusses=0
    for row in grid:
        total = sum(row)
        if total%13==0:
            bonusses += total/13

    for col_index in range(shops):
        total = 0
        for row_index in range(days):
            total += grid[row_index][col_index]
        if total%13==0:
            bonusses += total/13




    print(int(bonusses))

