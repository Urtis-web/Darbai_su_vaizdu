# Use romeo.txt as the file name
fname = input("Enter file name: ")
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))
pilna_eilute = []
nauja_eilute = []
new_list = []
for line in fh :                               #
    eilute = line.split()                      # iraso viena teksto eilute i kintamaji
    print(eilute)                              # isveda i ekrana viena eilute
    pilna_eilute = pilna_eilute + eilute       # prideda po viena eilute i bendra/ilga eilute
print(pilna_eilute)                            # isveda i ekrana pilna eilute
def funkcija():                                # pradedam funkcija
    pirmas = True                              # numatomas atminties kintamasis pirmam kartui //flegas
    for x in pilna_eilute:                     #
        if pirmas == True:                     # pirma karta pirmas yra true
            nauja_eilute.append(x)             # prie nauja_eilute pridedamas pirmas zodis
            pirmas = False                     # ir flegas isjungiamas
        elif pirmas == False:                  # jeigu flgas isjungtas
            if x in nauja_eilute:              # jeigu x(zodis) yra masyve nauja_eilute
                continue                       # persokam i virsu ir tesiam darba
            elif x not in nauja_eilute:        # jeigu x(zodzio) nera masyve nauja_eilute
                nauja_eilute.append(x)         # pridedam zodi i masyva nauja_eilute
    return(nauja_eilute)                       # grazinam galutine reiksme i funkcija()
bum = funkcija()                               #
r = sorted(bum)                                # r kintamajam priskiriamas naujas (bum surusiuotas) masyvas
print(r)                                       # isrykiuotas masyvas isvedamas i ekrana

