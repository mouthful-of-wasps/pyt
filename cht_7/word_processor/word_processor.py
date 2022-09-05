input_doc = open(file='word.in', mode='r')
output_doc = open('word.out','w')

options = input_doc.readline().split()

nos_words = int(options[0])
max_non_blank_characters_per_line = int(options[1])
words = input_doc.readline().split()

line = ''
current_nos_characters = 0

def save_line(a_string:str):
    output_doc.write(f'{line[:-1]}\n')

for word in words:
    len_word = len(word)
    if current_nos_characters + len_word <= max_non_blank_characters_per_line:
        line += f'{word} '
        current_nos_characters += len_word
    else:
        save_line(line)
        line = f'{word} '
        current_nos_characters = len_word

save_line(line)

input_doc.close()
output_doc.close()