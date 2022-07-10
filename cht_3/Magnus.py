# coci18c3p1

# Magnus lost a game of chess to Kile so he found comfort in competitive programming. Very soon, he heard of the iconic COCI competition and decided to try his luck there.

# He wrote a mail to Kile: "Dear Kile, please, prepare me for COCI. Magnus".

# Kile replied: "You want to participate in COCI? All right, here's your warm-up task. A series of four consecutive 
# letters of some word that make up the subword HONI (Croatian acronym for COCI) is called the HONI-block. I will send you the word of length N N and you will 
# throw out as many letters as you want (it might be none as well) so that in the end there are as many HONI-blocks as possible in the word. Kile".

# Magnus was very worried and asked you, COCI competitive scene, for help. Help him determine the maximum number of HONI-blocks he can get in the final word.
# Input

# The first line contains a word of length N N ( 1 ≤ N ≤ 100 000 ) (1 \le N \le 100\,000) , consisting of uppercase letters of the English alphabet.
# Output

# In the first and only line, print out the required number of HONI-blocks.




input_text = input()

HONI = 0

letter = 1

for character in input_text:
    if (letter == 1 and character == 'H'):
        letter = 2
    elif (letter == 2 and character == 'O'):
        letter = 3
    elif (letter == 3 and character == 'N'):
        letter = 4
    elif (letter == 4 and character == 'I'):
        HONI += 1
        letter = 1


print(HONI)
    