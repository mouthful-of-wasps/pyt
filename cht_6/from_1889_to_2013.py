#DMOJ problem ccc13s1, From 1987 to 2013




def distinct(year):
     
    if year > 9875:
        return 10234
    
    year += 1
    my_set = len(set(str(year)))
    my_list = len(list(str(year)))

    if my_set == my_list:
        #print(year)
        return year
    
    return distinct(year)


print(distinct(int(input())))