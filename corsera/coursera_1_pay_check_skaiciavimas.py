hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)
Hlimit = input("Enter what is normal working limit?:")
hlimit = float(Hlimit)
Hover = 0
paycheck = 0
regulartime = 0
iregulartime = 0
if h > hlimit:
    Hover = h - hlimit
    regulartime = hlimit * r
    iregulartime = Hover * (r * 1.5)
    paycheck = regulartime + iregulartime
else :
    paycheck = h * r
print(paycheck)