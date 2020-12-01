
#######################################################
hrs = input("Enter Hours:")
try:
    hours = float(hrs)
except:
    print("You can enter only a digit :(")
    Quit()
#######################################################
rat = input("Enter Rate:")
try:
    rate = float(rat)
except:
    print("You can enter only a digit :(")
    Quit()
#######################################################
def computepay(hours,rate):
    if hours > 40 :
        left = hours - 40
        left = left * rate/2
        fullpart = hours * rate
        totally = left + fullpart
        return(totally)
    elif hours <= 40 :
        totally = hours * rate
        return(totally)
    else :
        print("error")


print("Pay",computepay(hours,rate))