#Now to count words from a file using the dictionary

name = input('Enter file:')                     #ask filename
handle = open(name)                             #open filename in filehandler called handle

counts = dict()                                 #create dictionary called counts
for line in handle:                             #for every iteration(line) in handle
    words = line.split()                        #create a new variable called words, and put the lines split into seperate words into it
    for word in words:                          #for every iteration(word) in the list words
        counts[word] = counts.get(word, 0) + 1  #check to see if the word is in the dictionary, if NO then add it and give value 0, then add 1
                                                #If YES, take the value and add one to it
#################################################Histogram is now generated: it is stored in 'counts'

bigcount = None                                 #create variable bigcount which is empty
bigword = None                                  #create variable bigword which is empty
                                                #We've written programs to find the largest value in a list before. Now, we want to find the largest VALUE in a key:value pair
for word,count in counts.items():               #for every TWO iteration variables (word and count) in the TWO variables which are returned
                                                #by the items() method, namely the key:value pair
    if bigcount is None or count > bigcount:    #check whether the bigcount variable is empty, or whether whether the count variable is greater than the bigcount variable
                                                #remember: the histogram is already generated, so the items list already holds all the counts,
                                                #so this simply checks whether the current item being reviewed is higher than the current highest (or bignumber)
        bigword = word                          #If this is true, the current value under review becomes the new bigword
        bigcount = count                        #Same for bigcount

print(bigword,bigcount)
print(counts)                  #Print the results
