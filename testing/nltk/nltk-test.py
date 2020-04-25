#Adapted from Pythonprogramming.net nltk PoS tagging tutorial
import nltk
from nltk import pos_tag
from nltk import RegexpParser
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
title = "MicroRNA-182 suppresses clear cell renal cell carcinoma migration and invasion by targeting IGF1R"

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(title)
def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
            gram = "NP: {<NN.?>*<VBZ.?>*}"
            cp = nltk.RegexpParser(gram)
            result = cp.parse(tagged)

            result.draw()
    except Exception as e:
        print(str(e))


process_content()
