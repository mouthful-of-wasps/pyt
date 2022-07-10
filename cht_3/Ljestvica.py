# for at sequence of notes seperated by |
# A-dur A , D , and E , 
#  C-dur C , F , and G
# if equal the last note decides
 

music = input()

a_mol=0
c_dur=0

amol = 'ADE'
cdur = 'CFG'

new_note =True


for i in range(len(music)):

    if new_note:
        if music[i] in amol:
            a_mol +=1
            
        elif music[i] in cdur:
            c_dur +=1

        new_note = False

    elif music[i] == '|':
        new_note = True



if c_dur==a_mol:
    if music[-1] in amol:
            a_mol +=1
            
    elif music[-1] in cdur:
            c_dur +=1 


if c_dur > a_mol:
    print('C-dur')
elif a_mol> c_dur:
    print('A-mol')