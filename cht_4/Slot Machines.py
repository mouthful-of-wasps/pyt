quarters = int(input())
first = int(input())
second = int(input())
third = int(input())
pulls = 0
machine = 0


#if first == 35:
#    first =1
#if second ==100:
#    second =1
#if third ==10:
#    third=1

while quarters > 0:
    
    if machine%3==0:
            
            first += 1
            if first%35==0:
              quarters+=30
            
            

    elif machine%3==1:
           
            second+=1
            if second%100==0:
              quarters+=60
            
            
    else:
            
            third +=1
            if third%10 == 0:
              quarters+=9

    
    machine+=1            
    quarters -= 1
    pulls+=1


print('Martha plays ' + str(pulls) + ' times before going broke.')