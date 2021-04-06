#WILD CARD CHARACTERS
#DOT for example matches ANY character
#ASTERISK is "Any number of times"

# so a line like :
#  re.search('^X.*:')
# Search for a line, that starts with (^) 'X' (X) then matches any character (.) any number of times (*) until it finds a colon (:)

import re

fhand = open('tinytext.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)

# This prints all three lines in tinytext.txt
# However, suppose we don't want the final line, it just happens to match
#Then we try to find a pattern that exclused that line
# In this case, only the last line contains white space between X and the colon:
#So we can exclude whitespace from our search using \S which stands for 'Match any non-whitespace character'
# and + which stands for 'One or more times'
# The line becomes (^X-\S+:)
# Or: Match the start of the line (^) with 'X-' followed by any NON-WHITESPACE character (\S) one or more times (+) upto colon (:)

print("NOW FILTERED BETTER:")
fhand = open('tinytext.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)
