#So now, what do we do with a webpage once we've retrieved it into our program
# We call this WEB SCRAPING, or WEB SPIDERING
# Not all website are happy to be scraped, quite a few don't want a 'robot' scraping their content
# They can ban you (account or IP) if they detect you scraping, so be careful when playing around with this.

#now onto PARSING HTML. It is difficult! You can search string manually but the internet is FULL of BAD HTML
#Errors everywhere
#FORTUNATELY, there is some software called Beautiful Soup which basically says, 'give me the HTML link and I'll return you the tags'

#I already have Beautful Soup 4 (BS4) installed.
# To call it we need to import it

import urllib.request, urllib.parse, urllib.error   # First the same stuff we did earlier:
from bs4 import BeautifulSoup                       # and then BS4

# Now to write a simple program with BS4. NOTE: Beautiful Soup is a COMPLEX library. I'll do something simple here, but I might need to
# read up on the documentation if I want to use it more in depth.

url = input('Enter - ')
html = urllib.request.urlopen(url).read()       #read() here means read the WHOLE thing, which is ok if you know the file is not so large
                                                #This return a BYTES object and places it in HTML. BS4 knows how to deal with BYTES
soup = BeautifulSoup(html, 'html.parser')       #Here we call BS4 and say, hey use the stuff in the variable html, and use your html.parser on it,
                                                # place the results in soup

# Retrieve all of the anchor tags
tags = soup('a')                        #Here we call the soup object we just made (or BS4 made for us), and sort of call it like a function,
                                        #The 'a' instruction says, hey give me the anchor tags in soup, and then place them in 'tags'
                                        #Anchor tags are HYPERLINKS, by the way, this wasn't explained, you're basically extracting a LINK
                                        # from the HTML.
for tag in tags:
    print(tag.get('href', None))        #href is the tag used in HTML to indicate a hyperlink, so in the HTML code it is
                                        # <a href="http://www.dr-chuck.com/page2.htm"> Second Page</a>
                                        #That's why we're 'getting' the href part, so it prints the actual URL and nothing else
                                        # Although I'm not sure exactly how that works
