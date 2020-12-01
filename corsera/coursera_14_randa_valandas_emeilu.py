fname = input("Enter file name: ")                                                           # nurodomas inputas
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))       # atidarome faile
########################################################################################
counts = dict()                                                                              # sukuriame tuscia dictionarie
for line in fh:                                                                              # ieskome per visas failo eilutes
    if line.startswith('From '):                                                             # jeigu eilute prasideda 'From '
        words = line.split()                                                                 # irasome atskirtus zodzius i kintamaji
        hour = words[5]                                                                      # paimame 5 zodi
        counts[hour[:2]] = counts.get(hour[:2],0) + 1                                        # susumuojame kiek kartu pasikartoja tie patys zodziai(dvieju simboliu ilgio)
#print(counts)
for key, val in sorted(counts.items()):
    print(key,val)
########################################################################################
# kad uzkomentuoti viska reikia apvesti ir laikant nuspaudus spausti ------>>> ctrl /
