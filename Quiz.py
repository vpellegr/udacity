"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    wordlist = s.split()
    wordfreq = [wordlist.count(w) for w in wordlist]
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    d = dict(zip(wordlist,wordfreq))
    aux = [(key,d[key]) for key in d]
    from operator import itemgetter, attrgetter, methodcaller
    aux = sorted(aux, key=itemgetter(1), reverse=True)
    freq = [pair[1] for pair in aux]
    m = len(freq)
    for i in range(0,m-1):
        if freq[i] != freq[i+1]:
            list1 = aux[0:i+1]
            list2 = aux[i+1:m]
            list2 = sorted(list2, key=itemgetter(0), reverse=True)
            list2 = list2[::-1]
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = list1 + list2
    top_n = top_n[0:n]

    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)
    print count_words("london bridge is falling down falling down falling down london bridge is falling down my fair lady", 5)

if __name__ == '__main__':
    test_run()
