fname = input("Enter file name: ")                                                           # nurodomas inputas
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))       # atidarome faile
########################################################################################
counts = dict()                                                                              # sukuriame tuscia dictionarie
for line in fh:                                                                              # ieskome per visas failo eilutes
    words = line.split()                                                                     # irasome atskirtus zodzius i kintamaji
    for word in words:                                                                       # ieskome atskirai kiekviena zodi
        counts[word] = counts.get(word,0) + 1                                                # susumuojame kiek kartu pasikartoja tie patys zodziai
########################################################################################
print(sorted( [ (v,k) for k,v in counts.items() ] ) )
#    [  sukuria v,k tuples keliaudamas for loopu per visas list count reiksmes       ]