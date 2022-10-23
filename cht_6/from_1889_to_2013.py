#DMOJ problem ccc13s1, From 1987 to 2013




def distinct(year):
     
    if year > 9876:
        return f'There are no more years with distinct numbers'
    
    year += 1
    my_set = len(set(str(year)))
    my_list = len(list(str(year)))

    if my_set == my_list:
        #print(year)
        return year
    
    return distinct(year)


print(distinct(int(input('Write a year between 0 and 10000, to see the next year with distinct numbers!'))))