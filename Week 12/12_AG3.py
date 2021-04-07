import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def extracttag(numofloops):
    count = 0
    tags = soup('a')
    for tag in tags:
        count += 1
        if count == numofloops:
            break
    tag = str(tag)
    tag = tag.split('"')
    newlink = tag[1]
    return newlink

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
usercount = input('Enter count: ')
userpos = input('Enter position: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

loops = 0

while loops < int(usercount):

    exttag = extracttag(int(userpos))
    print(exttag)
    url = exttag
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    loops += 1
