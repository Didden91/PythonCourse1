# Now moving on to JSON. We need to import the json library to use it

import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

#In JSON the syntax is curly braces instead of the <> angle brackets of XML
#JSON represnets ata as nested "lists" and "dictionaries"
#Within the curly braces you'll find key/value pairs like "name" : "Chuck"
#You can also have objects within objects such as the type and number within phone

#We're going to load all the data into a variable called info

info = json.loads(data) #call the json library, with the method .loads (is load s, or "load from string") on the string 'data'

#This action returns us a DICTIONARY, so 'info' is now a dictionary
#It becomes a dictionary BECAUSE THE FIRST CHARACTER IN THE STRING IS A CURLY BRACE
#Because it's a dictionary we can apply the same syntax we have done earlier on dictionaries and call a 'sub'
#So with a list or dictionary we can just call list[1] to get the item in slot 1 of the list, the same applies here,
#You just call the title of the subitem you're looking for
print('Name:', info["name"]) #Here we ask: what's in the value in the key 'name', it returns 'chuck'
print('Hide:', info["email"]["hide"]) #here we ask, what's the value of the key hide, within the key email, it returns 'yes'
