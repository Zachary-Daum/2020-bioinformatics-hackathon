#parse for between two variables | Credit to dotnetperls
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

   #working w/ multiple files
    n = 1
    while ( n <= 2 ):
        workingfile = "test-data{}.txt"
        workingfile = workingfile.format(n)

        #get data
        with open(workingfile,'r') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            if "names ml" in temp:
                #w/out affiliations
                authors = between(temp, 'names ml {          "', '"        }      },').replace('",          "',"-")
                #list author's names
                authorlist = authors.split("-")
                print(authorlist)

                #still need to find lookup method for authors
                n = n+1
        
            else:
                #get needed data
                data = between(temp, "names std {          {",'          }        }      },      from journal').replace('."          },          {            name ml ','-').replace('",            affil str "','-').replace('            name ml "','').replace('"','')
                datasplit = data.split("-")
                #find each author
                AUTH = datasplit[0::2]
                #find each author's affiliations
                AFF = datasplit[1::2]
                print(AUTH)
                print(AFF)

                #lookup authors and affiliations and compile in other doc
                n = n+1
        
