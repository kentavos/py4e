#exercise 3.3


score = input("Enter a value between 0.0 and 1.0: ")
try:
    score = float(score)
except:
    print('Use Numerals Only.')
    quit()

if score >= .9:
    print("A")

elif score >= .8:
    print("B")

elif score >= .7:
    print("C")

elif score >= .6:
    print("D")

elif score < .6:
    print("F")

print ('All Done')
