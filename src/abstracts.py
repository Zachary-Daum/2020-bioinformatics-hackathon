import nltk
from nltk import pos_tag
from nltk import RegexpParser
import matplotlib.pyplot as plt

def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.rfind(b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]
#create file names to draw data from
with open('data/fake_pmids.txt', 'r') as fakeid:
    fakeid = fakeid.readlines()
    fakeid = ''.join(fakeid).replace("PMID:","")
    idlist = fakeid.splitlines() #by here each PMID is its own item in the list

    n = 0
    #create lists
    CCperWlist = []
    INperWlist = []
    JJperWlist = []
    RBperWlist = []
    JJperNNlist = []
    RBperVBlist = []
    WperSlist = []
    SentStdevlist = []
    
    while ( n <= 421 ):
        workingid = idlist[n]
        workingfile = "data/fakes/{}.txt"
        currentfile = workingfile.format(workingid)
        with open (currentfile, 'rt') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            abstract = between(temp,'abstract "','.",    mesh {')
            #word count
            wdcount = (len(abstract.split()))

            #sentence count
            senscount = (len(abstract.split('.')))

            text = abstract.split()
            tagged = pos_tag(text)
            temp = str(tagged).strip('[]')
            if wdcount == 0:
                new_CCperWlist = 0
                new_INperWlist = 0
                new_RBperWlist = 0
            else:
            #Count Parts of Speech
                CCCount = temp.count('CC')
                INCount = temp.count('IN')
                JJCount = temp.count('JJ')
                RBCount = temp.count('RB')
                NNCount = temp.count('NN')
                VBCount = temp.count('VB')

                new_CCperWlist = CCCount / wdcount
                CCperWlist.append(new_CCperWlist)
                new_INperWlist = INCount / wdcount
                INperWlist.append(new_INperWlist)
                new_JJperWlist = JJCount / wdcount
                JJperWlist.append(new_JJperWlist)
                new_RBperWlist = RBCount / wdcount
                RBperWlist.append(new_RBperWlist)
                new_JJperNNlist = JJCount / NNCount
                JJperNNlist.append(new_JJperNNlist)
                new_RBperVBlist = RBCount / VBCount
                RBperVBlist.append(new_RBperVBlist)
                new_WperSlist = wdcount / senscount
                WperSlist.append(new_WperSlist)
            #find stdev of length of sentences###
            
        n = n+1

 ##plotting
    plt.subplot(321)
    plt.scatter(WperSlist, CCperWlist, c = "red", alpha=0.5)
    plt.ylabel('Coordinating Conjunctions Per Word')
    plt.xlabel('Words Per Sentence')
    
    plt.subplot(322)
    plt.scatter(WperSlist, INperWlist, c = "red", alpha=0.5)
    plt.ylabel('Subordinating Conjunctions Per Word')
    plt.xlabel('Words Per Sentence')
    
    plt.subplot(323)
    plt.scatter(JJperWlist, RBperWlist, c = "red", alpha=0.5)
    plt.ylabel('Adjectives Per Word')
    plt.xlabel('Adverbs Per Word')
    
    plt.subplot(324)
    plt.scatter(WperSlist, JJperNNlist, c = "red", alpha=0.5)
    plt.ylabel('Adjectives Per Noun')
    plt.xlabel('Words Per Sentence')
    
    plt.subplot(325)
    plt.scatter(WperSlist, RBperVBlist, c = "red", alpha=0.5)
    plt.ylabel('Adverbs Per Verb')
    plt.xlabel('Words Per Sentence')

####################################REAL DATA###################
with open('data/rand_pmids.txt', 'r') as fakeid:
    fakeid = fakeid.readlines()
    fakeid = ''.join(fakeid).replace("PMID:","")
    idlist = fakeid.splitlines() #by here each PMID is its own item in the list

    n = 0
    #create lists
    CCperWlist = []
    INperWlist = []
    JJperWlist = []
    RBperWlist = []
    JJperNNlist = []
    RBperVBlist = []
    WperSlist = []
    SentStdevlist = []
    
    while ( n <= 140 ):
        workingid = idlist[n]
        workingfile = "data/rand/{}.txt"
        currentfile = workingfile.format(workingid)
        with open (currentfile, 'rt') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            abstract = between(temp,'abstract "','.",    mesh {')
            #word count
            wdcount = (len(abstract.split()))

            #sentence count
            senscount = (len(abstract.split('.')))

            text = abstract.split()
            tagged = pos_tag(text)
            temp = str(tagged).strip('[]')
            if wdcount == 0:
                new_CCperWlist = 0
                new_INperWlist = 0
                new_RBperWlist = 0
            else:
            #Count Parts of Speech
                CCCount = temp.count('CC')
                INCount = temp.count('IN')
                JJCount = temp.count('JJ')
                RBCount = temp.count('RB')
                NNCount = temp.count('NN')
                VBCount = temp.count('VB')

                new_CCperWlist = CCCount / wdcount
                CCperWlist.append(new_CCperWlist)
                new_INperWlist = INCount / wdcount
                INperWlist.append(new_INperWlist)
                new_JJperWlist = JJCount / wdcount
                JJperWlist.append(new_JJperWlist)
                new_RBperWlist = RBCount / wdcount
                RBperWlist.append(new_RBperWlist)
                new_JJperNNlist = JJCount / NNCount
                JJperNNlist.append(new_JJperNNlist)
                new_RBperVBlist = RBCount / VBCount
                RBperVBlist.append(new_RBperVBlist)
                new_WperSlist = wdcount / senscount
                WperSlist.append(new_WperSlist)
            #find stdev of length of sentences###
            
        n = n+1

 ##plotting
    plt.subplot(321)
    plt.scatter(WperSlist, CCperWlist, c = "blue", alpha=0.5)
    plt.ylabel('Coordinating Conjunctions Per Word')
    plt.xlabel('Words Per Sentence')
    
    plt.subplot(322)
    plt.scatter(WperSlist, INperWlist, c = "blue", alpha=0.5)
    plt.ylabel('Subordinating Conjunctions Per Word')
    plt.xlabel('Words Per Sentence')
    
    plt.subplot(323)
    plt.scatter(JJperWlist, RBperWlist, c = "blue", alpha=0.5)
    plt.ylabel('Adjectives Per Word')
    plt.xlabel('Adverbs Per Word')
    
    plt.subplot(324)
    plt.scatter(WperSlist, JJperNNlist, c = "blue", alpha=0.5)
    plt.ylabel('Adjectives Per Noun')
    plt.xlabel('Words Per Sentence')
    
    plt.subplot(325)
    plt.scatter(WperSlist, RBperVBlist, c = "blue", alpha=0.5)
    plt.ylabel('Adverbs Per Verb')
    plt.xlabel('Words Per Sentence')
    
    plt.show()
    
            
