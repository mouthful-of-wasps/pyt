# coci16c1p1

# Pero has negotiated a Very Good data plan with his internet provider. The provider will let Pero use up X X megabytes to surf the internet per month. Each megabyte that he doesn't spend in that month gets transferred to the next month and can still be spent. Of course, Pero can only spend the megabytes he actually has.

# If we know how many megabytes Pero has spent in each of the first N N months of using the plan, determine how many megabytes Pero will have available in the N + 1 N+1 month of using the plan.
# Input Specification

# The first line of input contains the integer X X ( 1 ≤ X ≤ 100 ) (1 \le X \le 100) .
# The second line of input contains the integer N N ( 1 ≤ N ≤ 100 ) (1 \le N \le 100) .
# Each of the following N N lines contains an integer P i P_i ( 0 ≤ P i ≤ 10 000 ) (0 \le P_i \le 10\,000) , the number of megabytes spent in each of the first N N months of using the plan. Numbers P i P_i will be such that Pero will never use more megabytes than he actually has.
# Output Specification

# The first and only line of output must contain the required value from the task.
# Sample Input 1
# Copy

# 10
# 3
# 4
# 6
# 2

# Sample Output 1
# Copy

# 28

mbs = int(input())
mnths = int(input())
available = 0
for i in range(mnths):
    available += mbs - int(input())


print(available+mbs)
