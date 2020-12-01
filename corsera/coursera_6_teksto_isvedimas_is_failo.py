# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(r"C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\corsera\{}".format(fname))
for line in fh :
    print(line.rstrip().upper()) #panaikina tarpa tarp eiluciu ir padaro visas raides didziasias
