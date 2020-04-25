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
    while ( n <= 20 ):
        workingid = idlist[n]
        workingfile = "test-data{}.txt"
        currentfile = workingfile.format(workingid)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                
            
        #get title names
        with open(workingfile, 'r') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            titles = between(temp, 'cit {          title {          name"', '"        }')
            print(titles)
   
            
=======
=======
>>>>>>> 2f99a7a2f6516691739c434e30e2a35316bdbf49
=======
>>>>>>> 2f99a7a2f6516691739c434e30e2a35316bdbf49
        with open (currentfile, 'rt') as file:
            data = file.read().splitlines()
            temp = ''.join(data)
            title = between(temp,'title {        name "','"      },      authors')
            titlelist = title.splitlines()
            print(titlelist)
                   
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2f99a7a2f6516691739c434e30e2a35316bdbf49
=======
>>>>>>> 2f99a7a2f6516691739c434e30e2a35316bdbf49
=======
>>>>>>> 2f99a7a2f6516691739c434e30e2a35316bdbf49
        n = n+1
