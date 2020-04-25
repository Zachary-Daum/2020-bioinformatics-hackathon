import nltk
from nltk import pos_tag
from nltk import RegexpParser
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

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
    VBlist = []
    VBZlist = []
    NNlist = []
    JJlist = []
    INlist = []
    JJperNN = []
    SLenList = []
    NNWlist = []
    while ( n <= 421):
        workingid = idlist[n]
        workingfile = "data/fakes/{}.txt"
        currentfile = workingfile.format(workingid)
        with open (currentfile, 'rt') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            title = between(temp,'title {        name "','."      },      authors {')
            #find sentence length
            sent_len = (len(title.split()))
            abstract = between(temp,'abstract "','.",    mesh {')
            #PoS Tagging
            tokenizedtitle = custom_sent_tokenizer.tokenize(title)
            def process_content():
                for i in tokenizedtitle:
                    words = nltk.word_tokenize(i)
                    tagged = nltk.pos_tag(words)
                        #process title
                    temp = str(tagged).strip('[]')
                        #count verbs
                    process_content.VBCount = temp.count('VB')
                        #count VBZ
                    process_content.VBZCount = temp.count('VBZ')
                        #count NN
                    process_content.NNCount = temp.count('NN')
                        #count JJ
                    process_content.JJCount = temp.count('JJ')
                        #count IN
                    process_content.INCount = temp.count('IN')

                    #count JJ/NN
                    if process_content.NNCount == 0:
                        process_content.JJperNN = 0
                    else:
                        process_content.JJperNN = process_content.JJCount / process_content.NNCount
                    
            process_content()

            VBlist.append(process_content.VBCount)
            JJperNN.append(process_content.JJperNN)
            #calc NN per S
            NNperW = process_content.NNCount / sent_len
            #append NN per S
            NNWlist.append(NNperW)
            n = n+1

    #plot everything
    plt.scatter( x = NNWlist, y = JJperNN, c = 'red')
    plt.scatter( x = VBlist, y = VBlist, c = 'blue')
    plt.xlabel('Nouns per Word')
    plt.ylabel('Adjectives per Noun')
    plt.show()
