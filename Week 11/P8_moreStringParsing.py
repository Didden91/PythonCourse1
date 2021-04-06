#let's make the previous example find something more specific
#Say I also want to pick what line to check, we can expand it to something like:

import re


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', data)
print(y)

#So we added ^From .*
#Which means, line has to start with 'From ' (including the space) followed by any character (.) for zero or more times (*) upto the @ sign (@)
#Prints the same as the previous one, but this one is much more precise, much less likely to pick up lines we don't want

#Now to turn a REGEX into a more useful program
#Once again, back to mbox-short!
#Let's look at the X-DSPAM-Confidence lines

import re                                                                   #Import regelur expressions
hand = open('mbox-short.txt')                                               #Open files and place in file handler 'hand'
numlist = list()                                                            #Create empty list called numlist
for line in hand:                                                           #For ever iteration (line) in teh file in the handler hand
    line = line.rstrip()                                                    #strip line
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)              #find all lines that: start with (^) 'X-DSPAM-Confidence: '  <-- this is the MATCHING or searching section
                                                                            #then EXTRACT: any digit or a dot [0-9.]
                                                                            #followed by one or more characters

    if len(stuff) != 1: continue                                            #If the length of stuff does not equal one (aka, stuff is empty), rerun the loop
    num = float(stuff[0])                                                   #Take the first entry of stuff, convert it to a floating point number, and place in num
    numlist.append(num)                                                     #add num to the list numlist
print('Maximum:', max(numlist))                                             #When all done, print the highest number in numlist

#Now, what if we want to use a special regular expression character as a NORMAL character you want to search for
# In most cases, you prefix it with a BACKSLASH \

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)                  #Search for an actual dollar sign, instead of whatever it is a dollar sign does
print(y)
