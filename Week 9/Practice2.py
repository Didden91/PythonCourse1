#COMMON USES OF DICTIONARIES
#Making a histograph, i.e. counting the frequency of things
#What we're going to solve here is, we can't just look at the data, we have to go through the data one at a time
#With dictionaries you can dynamically add e.g. names as they occur and keep track of each instance easily

#Tracebacks
#Referencing a KEY that is not in the dictionary gives you a traceback
#HOWEVER you can once again use the IN operator. It is the question "Is 'thisthing' in the dictionary?" and returns true or false
ccc = dict()
if 'csev' in ccc:
    print('yesss')
else:
    print('nooo')

#Again FOR loops are very useful in combination with IN and NOT IN

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    #for every iteration in names check if iteration is NOT IN dictionary
    #If it's not in, add that iteration to the dictionary using it's name as the key, and make the value 1, as it is the first instance of it
    if name not in counts:
        counts[name] = 1
    #If it is in: add one to the already stored value attached to that key
    else:
        counts[name] = counts[name] + 1
print(counts)

#HOWEVERRRRRRRR
#The above practice of checking to see if something is already in a dictionary and if not then adding it with a default value
#is so common, that dict() actually has a built in method for it, called GET
#can be used as nameofdict.get(KEY,DEFAULTVALUE)
#So instead of:
if name in counts:
    x = counts[name]
else:
    x = 0
#you can do
x = counts.get(name,0)

#Simplified countting with GET would go as follows. We can use GET() and provide
#the default value of zero when they key is not in the dictionary - and then just add one:

counts2 = dict()
names2 = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#For each iteration in the dictionary names2:
#GET the name of the iteration from the dictionary OR make the value the default (which is 0) if is NOT YET in the dictionary
# and then ADD one
#and place that back into the name of the iteration

#so first entry (iteration) is 'csev'
#calls method get('csev')
#It's not yet in the dictionary, so add to dictionary with default value = 0
#after this, add 1 to the value. 'csev' is now in dictionary with the value 1
#Second iteration is 'cwen', GET method is called: same story
#Third iteration is 'csev' again:
#calls method get('csev'). Found it, it is in the dictionary
#Therefore does NOT apply the default value, but rather says 'found it', it's value is currently 1
#Add 1 to the current value
#Next iteration

for iter in names2:
    counts2[iter] = counts2.get(iter, 0) + 1
print(counts2)
