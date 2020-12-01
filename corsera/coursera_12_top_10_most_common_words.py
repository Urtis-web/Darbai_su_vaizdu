fname = input("Enter file name: ")                                                           # nurodomas inputas
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))       # atidarome faile
########################################################################################
counts = dict()                                                                              # sukuriame tuscia dictionarie
for line in fh:                                                                              # ieskome per visas failo eilutes
    words = line.split()                                                                     # irasome atskirtus zodzius i kintamaji
    for word in words:                                                                       # ieskome atskirai kiekviena zodi
        counts[word] = counts.get(word,0) + 1                                                # susumuojame kiek kartu pasikartoja tie patys zodziai
########################################################################################
lst = list()
for key, val in counts.items():                                                              # is count dictionarie istraukiame key, val vertes
    newtup = (val, key)                                                                      # vertes irasome i tuple
    lst.append(newtup)                                                                       # prie saraso lst pridedame tople vertes

lst = sorted(lst,reverse=True)                                                               # surikiuojame sarasa pagal values(vertes) atvirkstine tvarka nuo didziausio iki maziausio

########################################################################################
for val, key in lst[:10]:                                                                    # keliaujam per 10 pirmu saraso verciu
    print(key,val)                                                                           # ir jas isvedame i ekrama