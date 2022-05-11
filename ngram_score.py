
#This version is written in Python 3

# Is your string English?  Useful when decoding ciphertext to see
# if  the recovered plaintext is actually English (i.e., correct)
#
#Allows scoring of text using n-gram probabilities
#17/07/12
#http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
#
#Changes to adapt to Python 3:
#(file() -> open(), xrange() -> range() and itervalues() -> values())
#
#
# To use, add these lines to your Python code:
# import ngram_score as ns
# fitness = ns.ngram_score('english_monograms.txt')  
# print fitness.score('HELLOWORLD')

# Instead of HELLOWORLD, replace with the code you want to test for
# English-ness.
# In addition to testing the code based on monograms, you can also use
# bigrams.txt, trigrams.txt, and quadgrams.txt

# This code works when the input is all CAPITAL letters


# **** USE CAPITAL LETTERS AS INPUT STRING ****
 


from math import log10

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        file = open (ngramfile)
        for line in file: #(ngramfile):
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)

        #self.N = sum(self.ngrams.itervalues())
        self.N = sum(self.ngrams.values())

        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__

        #for i in xrange(len(text)-self.L+1):
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       
