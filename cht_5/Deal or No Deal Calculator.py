#ccc07j3

monies = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]


cases = int(input())

for i in range(cases):
    monies[int(input())-1] = None




avg_left = sum(filter(None, monies ))/sum(x is not None for x in monies)
deal = int(input())

deal_txt = 'no deal' if avg_left > deal else 'deal'

print(
deal_txt
)