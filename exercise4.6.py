#Exercise 4.6

def computepay(hours, rate):
#    float(hours)
#    float(rate)
#    othours = hours-40
#    basepay = 40 * rate
#    otpay = othours * (rate*1.5)
#    totalpay = basepay + otpay
#    return totalpay


    if hours > 40:
        pay = ((hours-40)*(rate*1.5))+(rate *40)
    else:
        pay = (hours*rate)
    return pay

hours = input("Enter Hours:")
hours = float(hours)
rate = input("Enter Rate:")
rate = float(rate)
p = computepay(hours,rate)
print("Pay", p)
