s = 'betty bought a bit of butter but the butter was bitter'
wordlist = s.split()
wordfreq = [wordlist.count(w) for w in wordlist]
# TODO: Sort the occurences in descending order (alphabetically in case of ties)
d = dict(zip(wordlist,wordfreq))
aux = [(d[key],key) for key in d]
from operator import itemgetter, attrgetter, methodcaller
aux = sorted(aux, key=itemgetter(0), reverse=True)
print aux
freq = [pair[0] for pair in aux]
print freq
m = len(freq)
n = 3
for i in range(0,m-1):
    if freq[i] != freq[i+1]:
            print i
            list1 = aux[0:i+1]
            list2 = aux[i+1:m]
            list2 = sorted(list2, key=itemgetter(1), reverse=True)
            list2 = list2[::-1]
            list2 = list2[0:n]
            
# TODO: Return the top n words as a list of tuples (<word>, <count>)
list3 = list1 + list2
    
print list3
