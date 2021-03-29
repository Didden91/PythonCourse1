overtime = 0
extrapay = 0

hours = input("How many hours did you work? ")

try:
    hours = float(hours)
except:
    hours = -1

if hours < 0:
    print("Incorrect hours input")
    quit()

rate = input("What is your hourly rate? ")

try:
    rate = float(rate)
except:
    rate = -1

if rate < 0:
    print("Incorrect rate input")
    quit()

extrarate = float(rate) * 1.5
if float(hours) > 40:
    overtime = float(hours) - 40
    hours = 40
    extrapay = overtime * extrarate
pay = float(hours) * float(rate)
finalpay = pay + extrapay
print("Pay:",finalpay)
