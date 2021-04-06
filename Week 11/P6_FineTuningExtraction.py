#FINE TUNING EXTRACTION:
#We can now refine the terms withing re.findall() and seperately determine which portion we want to extract.
#Say we want the email address, we can use a line to say: find the @ character and extraxt
# everything left and right from the character until you find a space
# This would be: \S+@\S+
#Which translates to: A non-whitespace character (\S), At least one (+), followed by @ (@), followed by A non-whitespace character (\S), At least one (+)
#So that becomes:

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)

#This prints: ['stephen.marquard@uct.ac.za'] (as an item in a list)
#NOTE: If we were to add NON-GREEDY here, it would return 'd@u' because
# that is the shortest possible string taking a non-whitespace character on either side of the @ sign

#Now, suppose we want to search more accurately than just that string.
#We can use PARANTHESES for this!
#In parantheses we can write out what we want to EXTRACT
#While everything else is used for MATCHING (or finding) what you want.
#So building on what we have above:

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)

#This prints the exact same thing, but what it does, is FIRST make sure that it only uses lines starting with From followed by a space (^From )
# And only when that MATCHED, THEN extract whatever we've put in parantheses.
#In REGEX, parantheses say START EXTRACTION '(' and END extraction ')'
