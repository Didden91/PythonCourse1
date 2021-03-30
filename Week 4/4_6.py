
def computepay(hours, rate):
    overtime = 0
    extrapay = 0
    extrarate = float(rate) * 1.5
    if float(hours) > 40:
        overtime = float(hours) - 40
        hours = 40
        extrapay = overtime * extrarate
    pay = float(hours) * float(rate)
    finalpay = pay + extrapay
    return finalpay



h = input("How many hours did you work? ")

try:
    h = float(h)
except:
    h = -1

if h < 0:
    print("Incorrect hours input")
    quit()

r = input("What is your hourly rate? ")

try:
    r = float(r)
except:
    r = -1

if r < 0:
    print("Incorrect rate input")
    quit()

salary = computepay(h, r)
print("Your pay will be: ",salary)
