paint = int(input())
ltr_cap = int(input())
dollar_per_sold = int(input())


total_sales = (int(paint/ltr_cap) * dollar_per_sold ) + paint - (int(paint/ltr_cap) * ltr_cap) 

print(total_sales)