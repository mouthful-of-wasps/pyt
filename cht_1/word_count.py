import re
line = input()
total_words = re.sub(' {2,}', ' ',line).strip(' ').count(' ') +1

# print(total_words)

print('the line: ' + line + '\nhas a total of ' + str(total_words) + ' words')