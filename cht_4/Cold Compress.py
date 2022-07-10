#ccc19j3

no_lines = int(input())
i = 0

while i < no_lines:
    the_string = input()
    the_output = ''
    last_letter = ''
    letter = ''
    count = 0
    for ii in range(len(the_string)):
        if last_letter == '':
            last_letter = the_string[ii]
            count += 1
        else:
            if the_string[ii] == last_letter and (ii+1 < len(the_string)):
                count += 1
            elif  ii+1 < len(the_string):
                the_output = f'{the_output} {count} {last_letter}'
                count = 1
                last_letter = the_string[ii]
            else:
                if the_string[ii] == last_letter:
                    count += 1
                    the_output = f'{the_output} {count} {last_letter}'
                else:
                    the_output = f'{the_output} {count} {last_letter}' 
                    count = 1
                    the_output = f'{the_output} {count} {the_string[ii]}' 
    
    print(the_output[1:])    

    i+=1



