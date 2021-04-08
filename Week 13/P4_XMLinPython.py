#To use XML in Python we have to import a library called ElementTree

import xml.etree.ElementTree as ET #The as ET is a shortcut, very useful, makes calling it a lot simpler
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)      #create a object called tree, put the xml string information from 'data' in there
print('Name:', tree.find('name').text) #in the tree find the tag name, and return the whole text content (.text)
print('Attr:', tree.find('email').get('hide')) #in the tree find the tag email and get (.get) only the data in the attribute 'hide'

#Second example:

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
     </user>
    <user x="29">
      <id>1991</id>
      <name>Ivo</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')  # Creates a LIST called lst, and puts in there, every item it finds in the path users/user
                                    #In other words, in the users 'directory' return every item 'user' and put in the list
print('User count:', len(lst))

for item in lst:
    print(item)
    print('Name', item.find('name').text) #in the tree find the tag name, and return the whole text content (.text)
    print('Id', item.find('id').text)     #in the tree find the tag id, and return the whole text content (.text)
    print('Attribute', item.get('x'))     #in the tree find the attribute x and get (.get) only the data in the attribute
