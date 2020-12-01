fname = input("Enter file name: ")
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))
count = 0
for line in fh :                                    #
    if line.startswith('From '):                    # jeigu eilute prasideda 'From '
        eilute = line.split()                       # iraso viena teksto eilute i kintamaji
        count = count + 1                           # skaiciuoja tokius atvejus
        #print(eilute)                              # isveda i ekrana viena eilute
        el_pastas = eilute[1]                       # priskiria kintamajam eilutes 2 zodzio reiksme
        print(el_pastas)                            # isveda elpasta i ekrana
print("There were", count, "lines in the file with From as the first word")


#han = open('mbox-short.txt')

#for line in han
    #line = line.rstrip()
    #wds = line.split()
    #guardian
    #if len(wds) < 3 or wds[0] != 'From':
        #continue
    #print(wds[2])