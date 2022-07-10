#ccc18s1

n = int(input())

my_list = []

for i in range(n):
    my_list.append(int(input()))

my_list.sort()

smallest = my_list[-1] - my_list[0]
if len(my_list) >2:
    for i in range(1,len(my_list)-1):
       test = (my_list[i+1]-my_list[i-1])/2 
       if test < smallest:
           smallest = test
    


print(smallest)