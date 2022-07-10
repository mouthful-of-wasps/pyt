#coci08c3p2

import re 

hmm = input()

hmm = re.sub('apa','a',hmm)
hmm = re.sub('epe','e',hmm)
hmm = re.sub('ipi','i',hmm)
hmm = re.sub('opo','o',hmm)
hmm = re.sub('upu','u',hmm)

print(hmm)