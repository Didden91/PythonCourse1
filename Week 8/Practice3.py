#Many built-in functions can take lists as a parameter like max(), min(), len(), sum().
#You can build a similar program to what we did before to calculate the average of inputs through use of a list and these functions.

listofnum = list()

while True:
    numbers = input("Enter a number (enter 'done' when done): ")
    if numbers == 'done':
        break
    floatnum = float(numbers)
    listofnum.append(floatnum)

print(listofnum)

endresult = sum(listofnum) / len(listofnum)
print('sum of list is:', endresult)


poop = list()
poop.append(3)
print(len(poop))
