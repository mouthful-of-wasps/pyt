# Canadian Computing Competition: 2011 Stage 1, Senior #2

# Your teacher likes to give multiple choice tests. One benefit of giving these tests is that they are easy to mark, given an answer key. 
# The other benefit is that students believe they have a one-in-five chance of getting the correct answer, assuming the multiple choice possibilities are A, B, C, D or E.

# Write a program that your teacher can use to grade one multiple choice test.
# Input Specification

# The input will contain the number N N ( 0 < N < 10 000 0 < N < 10\,000 ) followed by 2 N 2N lines. 
# The 2 N 2N lines are composed of N N lines of student responses (with one of A, B, C, D or E on each line), 
# followed by N N lines of correct answers (with one of A, B, C, D or E on each line), in the same order as 
# the student answered the questions (that is, if line i i is the student response, then line N + i N+i will contain the correct answer to that question).
# Output Specification

# Output the integer C C ( 0 ≤ C ≤ N 0 \le C \le N ) which corresponds to the number of questions the student answered correctly.
# Sample Input 1
# Copy

# 3
# A
# B
# C
# A
# C
# B

# Output for Sample Input 1
# Copy

# 1

lines = int(input())
answer = ''
corr = ''

well_done = 0 

for i in range(lines):
    answer += input()

for i in range(lines):
    corr += input()


for i in range(len(corr)):
    if answer[i] == corr[i]:
        well_done += 1



print(well_done)
