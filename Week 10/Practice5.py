#Making a list of top 10 most common words in a file
#First part is a repeat of what I've done before:

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# This makes the histogram ^ and puts it in 'counts'

lst = list()                # make new list
for key,value in counts.items():
    newtupl = (value, key)  #Again we turn value and key AROUND here!
    lst.append(newtupl)      #add this turned around tuple value to (bottom of) the list

lst = sorted(lst, reverse=True) #make the list a sorted version of the list, in descending in stead of ascending order

for val, key in lst[:10]:       #for every iteration of value/key tuple, in the FIRST 10 entries of the list:
                                #sidenote: lst[:10] goes upto NOT including 10, BUT it starts with slot 0, so it is still the top 10
    print(key, val)             #print key value (NOTE: key and value are switched back here)

#THE ABOVE CODE for line 12 to 17 can actually be put into a SINGLE line
# suppose you have a dictionary that is:
c = {'a':10, 'b': 1, 'c':22}
#you can make a list, for loop through the list, flipping values and keys and returning a sorted version of the list in one go!
#That would look like this:

print(sorted([ (v,k) for k,v in c.items()]))

#You don't need to fully understand this yet, but the takeaway is, this is known as LIST COMPREHENSION
#Something Python does very well. You can write an expression in a place where python expects a list, and that expression will generate
#the required list on the fly.
