#Now to loop through files while using the dictionary!
#Let's try a counting pattern:
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()

print('Words:', words)
print('Counting...')
for word in words:
    #Again what this does is: check if a word is in the dictionary, if not, add and make value 0, and add 1, if yes, take value and add 1
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# TEST SENTENCE:
#the clown ran after the car and the car ran into the tent and the tent dell down on the clown and the car

#Definite loops and dictionaries:
#Even though dictionaries are not stored in order, we can make a loop that goes through each entry, or rather each KEY
# and looks up the value attached to that key

counts = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key]) #The first part 'key' prints the name of the key, the second part prints the value
                            #This is because counts[key] is basically asking, in the dictionary 'counts', what's the value of 'key'
                            #the first iteration would then print Jan 100
#RETRIEVING lists of the keys and values
#The above works for retrieving keys and values, but there are several other ways.
#You can turn a dictionary into a list and print it to get the KEYS
testdic = {'Dit': 10, 'is' : 50, 'een' : 390, 'test' : -40}
print(list(testdic))
#You can also get a list of the keys by using the keys() method.
print(testdic.keys())
#You can get a list of the VALUES by using the values() method.
print(testdic.values())
#You can get BOTH by using the items() method, this returns the key:value pairs in tuples (<-- will be covered in next chapter)
print(testdic.items())
