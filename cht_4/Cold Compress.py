#ccc19j3

no_lines = int(input())
i = 0

while i < no_lines:
    stringen = input()
    outputten = ''
    last_letter = ''
    letter = ''
    count = 0
    for ii in range(len(stringen)):
        if last_letter == '':
            last_letter = stringen[ii]
            count += 1
        else:
            if stringen[ii] == last_letter and (ii+1 < len(stringen)):
                count += 1
            elif  ii+1 < len(stringen):
                outputten = f'{outputten} {count} {last_letter}'
                count = 1
                last_letter = stringen[ii]
            else:
                if stringen[ii] == last_letter:
                    count += 1
                    outputten = f'{outputten} {count} {last_letter}'
                else:
                    outputten = f'{outputten} {count} {last_letter}' 
                    count = 1
                    outputten = f'{outputten} {count} {stringen[ii]}' 
    
    print(outputten[1:])    

    i+=1



