sum = 0
count = 0
average = 0
numberentered = None

while True:

    usernumber = input("Enter a number: ")
    try:
        usernumber = float(usernumber)
        numberentered = True
    except:
        numberentered = False

    if numberentered == True:
        count = count + 1
        sum = sum + usernumber
        average = sum / count
        
    else:
        if usernumber == 'done' or usernumber == 'Done':
            print("Total entries:",count,"Sum of entries",sum,"Average of entries",average)
            quit()
        else:
            print("Invalid input")
            continue
