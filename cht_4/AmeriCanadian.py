#ccc02j2

vowels = ('a','e','o','u','i','y')

while True:
    word = input()
    if word == 'quit!' or len(word) > 64:
        break
    else:
        if word[-2:] == 'or' and len(word) > 4 and not word[-3] in vowels:
            print(f'{word[:-2]}our')
        else:
            print(word)
       