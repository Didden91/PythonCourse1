overtime = 0
extrapay = 0
hours = input("How many hours did you work? ")
rate = input("What is your hourly rate? ")
extrarate = float(rate) * 1.5
if float(hours) > 40:
    overtime = float(hours) - 40
    hours = 40
    extrapay = overtime * extrarate
pay = float(hours) * float(rate)
finalpay = pay + extrapay
print("Pay:",finalpay)
