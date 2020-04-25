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
    n = 0
    while ( n <= 20 ):
        workingid = idlist[n]
        workingfile = "data/{}.txt"
        workingfile = workingfile.format(workingid)

        #get data
        with open(workingfile,'r') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            if "names ml" in temp:
                print("no affiliation for", workingfile, end='\n')
                #still need to find lookup method for authors
                n = n+1
        
            else:
                #get needed data
                data  = ''.join(data)
                data = between(data,'names std {          {            ','          }        }      },      from journal').replace('            affil str ','name ml ').replace('          },          {            ','')
                datasplit = data.split('name ml ')
                #find each author
                AUTH = datasplit[1::2]
                #find each author's affiliations
                AFF = datasplit[0::2]
                AFF = AFF[1:]

                n = n+1
                #combine authors and affiliations into datatable

                #author lookup
                print(AUTH)
        
