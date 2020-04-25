import nltk
from nltk import pos_tag
from nltk import RegexpParser
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

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
    titlelist = []
    while ( n <= 20 ):
        workingid = idlist[n]
        workingfile = "data/{}.txt"
        currentfile = workingfile.format(workingid)
        with open (currentfile, 'rt') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            title = between(temp,'title {        name "','"      },      authors')
            
        #build lists into one
        workinglist = title.splitlines()
        titlelist = titlelist + workinglist
        n = n+1
    i = 0
    while ( i < n ):
        workingtitle = titlelist[i]
        print(workingtitle)
        #analyze PoS of titles
        tokenized = custom_sent_tokenizer.tokenize(workingtitle)
        def process_content():
            try:
                for k in tokenized[:5]:
                    words = nltk.word_tokenize(k)
                    tagged = nltk.pos_tag(words)
                    print(tagged)

            except Exception as e:
                print(str(e))
        process_content()
        
        i = i+1

        #find PoS percentages
        
        
