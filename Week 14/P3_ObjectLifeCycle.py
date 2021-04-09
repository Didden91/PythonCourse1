# Objects are created, used, and discarded
# We have special blocks of code (methods) that get called
# -  At the moment of creation (constructor)
# -  At the moment of destruction (destructor)
# Constructors are used a lot
# Destructors are seldom used

#
# The constructor and destructor are optional.
# The constructor is typically used to set up variables.
# The destructor is seldom used.

# Example:

class PartyAnimal:
   x = 0

   def __init__(self):
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)


#
#
# In object oriented programming, a constructor in a class is a special block of statements called when an object is created
#
# We can create LOTS of objects - the class is the template for the object
# We can store each distinct object in its own variable
# We call this having multiple instances of the same class
# Each instance has its own copy of the instance variables
#
# Constructors can have additional parameters.
# These can be used to set up instance variables for the particular instance of the class (i.e., for the particular object).
#
# Example:

class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()
