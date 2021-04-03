#split method can take a string, take out each word seperated by a space (technically all whitespaces, also tabs and newlines and such)
# and place them in a list
abc = 'dit is een test'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[1])
#in this way you can make a loop that takes a line of data, and goes through each word individually
udata = input('enter a couple of words:')
spldata = udata.split()
for iter in spldata:
    print(iter)

# Split can take what is called a DELIMITER within the brackets, basically an instruction which states what characters split should
# look to split between, e.g. .split(';')
line = 'poop;scoop;floop'
thingy = line.split(';')
print(thingy)
#Do note: split is smart about spaces and can interpret e.g. 10 consecutive spaces as a single split,
# but can't do this with delimited characters

#simple program to look for a specific part of a phrase, in this case the day of the week:
# in lines such as : From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #this removes characters at the end of string, in this case mostly newlines
    if not line.startswith('From ') : continue #Checks if line does not start with 'From', if it indeed does not it 'constinues',
    #'continue' meaning start the next iteration of the loop from the beginning without executing the rest of the script first
    words = line.split() #splits every word of the line into seperate words and puts them in a list
    print(words[2]) #print the item in slot 2 (so the third item). This is because we know the structure of the strings and we know this will be the day ofthe week.

#similarly we can make a double split pattern to get the address line from an email adress
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    wholeline = line.split()
    email = wholeline[1] #because we know where the email starts in the file, in slot 1 when we split it
    splitinpieces = email.split('@') #seperate the two parts of the email by @ sign
    print(splitinpieces[1]) #print slot 1 of the split pieces, a.k.a. the address
