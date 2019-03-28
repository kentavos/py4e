#exercise5.2.py

largest = 0
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue

    if largest is None :
        largest = fnum

    elif fnum > largest :
        largest = fnum

    if smallest is None :
        smallest = fnum

    elif fnum < smallest :
        smallest = fnum

smallest = int(smallest)
largest = int(largest)

#    print(fnum)
#    print(largest)
#    print(smallest)

print("Maximum is", largest)
print("Minimum is", smallest)
