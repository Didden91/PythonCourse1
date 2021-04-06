#WARNING: GREEDY MATCHING
#Repeat characters like * and + push OUTWARD in BOTH directions (referred to as greedy) to match THE LARGEST POSSIBLE STRING
#This can make your results different to what you want.
#Example:
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print (y)
#So you want to find 'From:', so you say, starts with (^) F (F), followed by any character (.) one or more times (+) upto the colon (:)
#This finds 'From:' but it also finds 'From: Using the :'
#If this occurs, it always chooses the LARGEST ONE to return, so be careful with that.

#You can SUPRESS this behaviour (of course) by using adding another character, the questionmark '?'
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)                 #Adding the ? to the + means one or more characters, BUT NOT GREEDY
print (y)

#NOT GREEDY just means it prefers the SHORTEST string rather than the largest one
