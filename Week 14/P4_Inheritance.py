# When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class
# and then add our own little bit to make our new class
#
# Another form of store and reuse
#
# Write once - reuse many times
#
# The new class (child) has all the capabilities of the old class (parent) - and then some more
#
# Again, for now this is just about learning TERMINOLOGY!
# I don't have to understand when to use this, why to use this etc. This is just to get a better grasp of the bigger picture
#
# With inheritance there is once again a hierarchical system!
# The original class is called the PARENT
# and the new class derived from it is called the CHILD
# SUBCLASSES are another word for this
#
# example:

class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, nam):
     self.name = nam
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

#Now FootballFan is a class which EXTENDS PartyAnimal. It has all the capabilities of PartyAnimal and MORE
#So FootballFan is an amalgamation of all this. It includes everything we see here.

class FootballFan(PartyAnimal):
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
j = FootballFan("Jim")

s.party()
j.party()
j.touchdown()
