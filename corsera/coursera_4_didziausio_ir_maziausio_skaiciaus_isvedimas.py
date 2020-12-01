largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done": break
    try:
        number = float(num)
    except:
        print("Invalid input")
        continue
    if smallest is None :
        smallest = number
    elif number < smallest :
        smallest = number
    elif largest is None :
        largest = number
    elif number > largest :
        largest = number

print("Maximum is", int(largest))
print("Minimum is", int(smallest))