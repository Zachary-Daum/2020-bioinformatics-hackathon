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

#get data
with open('test-data2.txt','r') as file:
    data = file.read().splitlines()
    temp = ''.join(data)
    if "names ml" in temp:
        #w/out affiliations
        authors = between(temp, 'names ml {          "', '"        }      },').replace('",          "',"-")
        #list author's names
        authorlist = authors.split("-")
        print(authorlist)
        
    else:
        #get needed data
        data = between(temp, "names std {          {",'          }        }      },      from journal').replace('."          },          {            name ml ','-').replace('",            affil str "','-').replace('            name ml "','').replace('"','')
        datasplit = data.split("-")
        #find each author
        AUTH = datasplit[0::2]
        #find each author's affiliations
        AFF = datasplit[1::2]

