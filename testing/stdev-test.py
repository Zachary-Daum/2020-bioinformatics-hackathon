import statistics
abstract="BACKGROUND: Positron emission tomography/computed tomography (PET/CT scan) has increasingly been used for management of lymphoma, however few and conflicting data have been provided in the setting of high dose therapy with autologous stem cell transplantation (ASCT) so far. METHODS: We retrospectively evaluated the outcome of 47 NHL patients who underwent ASCT for relapsed/refractory disease or high risk disease or partial response after first line treatment, with the aim of testing sensitivity, specificity, positive and negative prognostic value of PET/CT performed before and after ASCT. RESULTS: In our experience pre ASCT-PET/CT predicts outcome of non-Hodgkin's lymphoma patients with chemosensitive relapse, whereas post ASCT-PET showed a better prognostic value for relapsed disease. CONCLUSIONS: Results of our study, if confirmed by studies on a larger scale, could significantly contribute to design future trials and optimize the management of lymphoma patients"
sentences = abstract.split('.')
stop = len(sentences)
n = 0
sLenList = []
while ( n < stop ):
    new_sLength = len(sentences[n].split())
    sLenList.append(new_sLength)
    n = n+1

print(sLenList)

print(statistics.stdev(sLenList))
