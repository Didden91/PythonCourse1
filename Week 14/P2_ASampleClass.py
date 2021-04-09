# CLASS is the TEMPLATE
# OBJECT is the INSTANCE

class PartyAnimal:          # class is a reserved word
    x = 0                   # Each PartyAnimal objects has a bit of data

    def party(self) :           # Each PartyAnimal object has a bit of code
      self.x = self.x + 1
      print("So far",self.x)
#END OF CLASS DEFINITION

an = PartyAnimal()             # construct a PartyAnimal object and store in 'an'

an.party()                     # Tell the an object to run the party() code within it
an.party()                     #This equates to PartyAnimal.party(an)
an.party()                     #So by that logic, in the definition of party we see above the 'self' becomes an alias of 'an'
