sum = 0
count = 0
highestnum = None
lowestnum = None
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
        if lowestnum is None:
            lowestnum = usernumber
        elif lowestnum > usernumber:
            lowestnum = usernumber
        if highestnum is None:
            highestnum = usernumber
        elif highestnum < usernumber:
            highestnum = usernumber


    else:
        if usernumber == 'done' or usernumber == 'Done':
            print("Total entries:",count,"\nSum of entries",sum,"\nLowest Number:",lowestnum,"\nHighest number:",highestnum)
            quit()
        else:
            print("Invalid input")
            continue
