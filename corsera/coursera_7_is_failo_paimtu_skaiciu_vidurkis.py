# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))
line_count = 0
sksu = 0
for line in fh :
    if not line.startswith("X-DSPAM-Confidence:"): continue
    nulio_suradimas = line.find('0')                                     # surandama nulio vieta eiluteje
    nulis = line[nulio_suradimas:]                                       # teksto paemimas nuo nulio vietos iki pat eilutes galo
    sk = float(nulis)                                                    # paimto teksto pavertimas i float
    sksu = sksu + sk                                                     # skaiciu suma
    print('Paversti skaiciai-',sk,'      ','skaiciu suma-',sksu)
    line_count = line_count + 1                                          # paimtu eiluciu skaiciavimas
print('Average spam confidence:',sksu/line_count)                        # vidurkio isvedimas i ekrana





