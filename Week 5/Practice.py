import random

largestnum = -1
for number in [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]:
    print("Current number is:",number)
    if number > largestnum:
        largestnum = number
    print("largest so far:",largestnum)
print("The winner is:",largestnum)

counter = 0
print("Starting at 0!")
for thing in [56, 78, 'test', 5.78000000001]:
    counter = counter + 1
    print("This is loop:",counter,"     ",thing)

print("All done!")

sum = 0
count = 0
found = False
print("calculating sum")
for randnum in [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]:
    count = count + 1
    print("New number added is:",randnum)
    if randnum > 50:
        print("Found a LARGE ONE:",randnum)
    if randnum > 95:
        found = True
    print(sum,"+",randnum)
    print("This was loop:",count)
    sum = sum + randnum
print("Final result =",sum)
print("Final number of loops =",count)
print("Average number =",sum / count)
if found == True:
    print("Found a REAL BIG ONE, the found value is",found)
else:
    print("Did not find a big one :( the found value is",found)


smallest = None
print("Now to look for the smallest number")
for numbah in [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]:
    print("The number is:",numbah)
    if smallest is None:
        smallest = numbah
    elif numbah < smallest:
        smallest = numbah
print("The smallest of all the numbers is:",smallest)
