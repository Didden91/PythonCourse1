#A bit more complex of an example.
#Here data starts with a SQUARE BRACKET which means it will be turned into a LIST rather than a dictionary
#HOWEVER, WITHIN this list are two items in curly braces, which will become DICTIONARIES
#So it is a list, and within it are two dictionaries


import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# Notice that we have NO ATTRIBUTES. In this way JSON is simpler than XML.
# However, we can just add another item to the list, which can serve a similar function
