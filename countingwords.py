wordstring = 'betty bougth a bit of butter but the butter was bitter'
wordlist = wordstring.split()
#print wordlist
wordfreq = [wordlist.count(w) for w in wordlist]
#print wordfreq

def countwords(wordlist):
    # take string and freq of words and create a dictionary
    d = dict(zip(wordlist,wordfreq))
    return d

def ordering(d):
    aux = [(d[key],key) for key in d]
    sorting = aux.sort()
    reverse = aux.reverse()
    return reverse


#dictionary = countwords(wordlist)
#ordinato = sorted(dictionary[w] for dictionary[w] in dictionary.items())
#print ordinato

#list1 = ['3','4','1']
#list1.sort(key=int)
#print list1

#string = ['c','a','b']
#string.sort()
#print string


#import collections
#string = collections.namedtuple('string','freq word')
d = countwords(wordlist)
#best = sorted([string(f,w) for (w,f) in d.items()], reverse=True)
#print best
numordD = sorted([(d[x],x) for x in d], reverse=True)
newD = numordD[0]
for i in range (0,3)
    if numordD[i] = numordD[i+1]
        newD = [newD, numordD[i]]
        


numordD = [numordD[0] , numordD[1], numordD[2]] 
alphaordD = sorted((d[x],y) for y in d)



alphaordD = [alphaordD[0] , alphaordD[1], alphaordD[2]] 
print numordD
print alphaordD


#if numordD != alphaordD:
    
    

#print newD

    







#import collections
#ordD = collections.OrderedDict(sorted(d.items()))

#print orderedD
#print ordD

#for i in range(1,3):
 #   newd = newd + orderedD[i]

#for j in range(0,3):
#    if newd[i] == newd[i+1]
        
        




#import collections
#string = collections.OrderedDict(sorted(d.items()))
#print string

