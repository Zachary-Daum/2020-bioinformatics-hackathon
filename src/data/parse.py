import requests
#get PMIDs
with open('rand_pmids.txt', 'r') as fakeid:
    fakeid = fakeid.readlines()
    fakeid = ''.join(fakeid).replace("PMID:","")
    idlist = fakeid.splitlines() #by here each PMID is its own item in the list

    n = 0
    while ( n <= 499 ):
        workingid = idlist[n]
        #creates proper filename
        workingfile = "rand/{}.txt"
        workingfile = workingfile.format(workingid)
        #creates correct link for metadata get
        workinglink = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={}"
        workinglink = workinglink.format(workingid)
        #request metadata
        request = requests.get(workinglink)
        request = request.text
        new = open(workingfile,"x")
        f = open(workingfile,"w")
        f.write(request)
        f.close()
        
        n = n+1

