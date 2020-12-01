fname = input("Enter file name: ")                                                           # nurodomas inputas
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))       # atidarome faile
########################################################################################
counts = dict()                                                                              # sukuriame tuscia dictionarie
for line in fh:                                                                              # ieskome per visas failo eilutes
    words = line.split()                                                                     # irasome atskirtus zodzius i kintamaji
    for word in words:                                                                       # ieskome atskirai kiekviena zodi
        counts[word] = counts.get(word,0) + 1                                                # susumuojame kiek kartu pasikartoja tie patys zodziai
########################################################################################
bigcount = None                                                                              # didziausiam skaiciui
bigword = None                                                                               # daugiausiai panaudotam zodziui
for word,count in counts.items():                                                            #
    if bigcount is None or count > bigcount :                                                # jeigu pirmas kartas arba jeigu verte didesne negu pries tai buvusi
        bigword = word                                                                       # atsimename zodi
        bigcount = count                                                                     # atsimename skaiciu
########################################################################################
print(bigword,bigcount)                                                                      #