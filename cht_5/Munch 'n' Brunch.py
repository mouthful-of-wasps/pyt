for i in range(0,10):
    trip_cost = int(input())*2
    payment = [12,10,7,5]

# amount_ppl_str = input().split(' ')


    amount_ppl = [float(num) for num in input().split(' ')]
    max_value = max(amount_ppl)
    max_index = amount_ppl.index(max_value)

    total_students = float(input())

    wow = []
    extra_ppl = 0
    for _ in range(len(amount_ppl)):
        if amount_ppl[_] > 0:     
            wow.append(int(total_students/(1/amount_ppl[_])))
        else:
            wow.append(0)
    if sum(wow) < total_students:
        wow[max_index] += total_students-sum(wow)

    for _ in range(len(wow)):
        extra_ppl += (wow[_]*payment[_])

    extra_monies = 'YES' if extra_ppl < trip_cost else 'NO'

    print(extra_monies)