wordstring = 'betty bought a bit of butter but the butter was bitter'
wordlist = wordstring.split()

from collections import Counter

lines = wordlist
words = [ w for l in lines for w in l.rstrip().split() ]

counts = Counter( words )

newlist = sorted(counts.most_common(), key=lambda (w, c): (c, w), reverse=True)
print newlist
freq = [pair[1] for pair in newlist]
m = len(freq)
n = 3
for i in range(0,m-1):
    if freq[i] != freq[i+1]:
        list1 = newlist[0:i+1] 
        list1 = list1[::-1]
        list2 = newlist[i+1:m]
        list2 = list2[::-1]
        list2 = list2[0:n]

list3 = list1 + list2
    
print list3



