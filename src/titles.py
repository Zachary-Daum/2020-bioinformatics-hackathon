#create file names to draw data from
with open('data/fake_pmids.txt', 'r') as fakeid:
    fakeid = fakeid.readlines()
    fakeid = ''.join(fakeid).replace("PMID:","")
    idlist = fakeid.splitlines() #by here each PMID is its own item in the list

    n = 0
    while ( n <= 0 ):
        workingid = idlist[n]
        workingfile = "data/{}.txt"
        currentfile = workingfile.format(workingid)
        with open (currentfile, 'rt') as file:
            for line in file:
                print(line[31])
                
            
        #get title names
        
   
            
        n = n+1
        
