score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("You can enter only a digit :(")
    Quit()
if s >= 0:
    if s <= 1:
        if (s < 0.6):
            print("You get a F for your score!")
        elif s >= 0.6 and s <0.7:
            print("You get a D for your score!")
        elif s >= 0.7 and s < 0.8:
            print("You get a C for your score!")
        elif s >= 0.8 and s < 0.9:
            print("B")
        elif s >= 0.9 and s <= 1:
            print("You get a A for your score!")
    else:
        print("Your entered value is not in [0:1] range!")
else:
    print("Your entered value is not in [0:1] range!")
