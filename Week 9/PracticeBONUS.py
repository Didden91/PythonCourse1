testdic = {'Dit': 10, 'is' : 50, 'een' : 390, 'test' : -40}
print(testdic.items())

#BONUS: You can use TWO iteration variables in a loop!
#The items() methods returns two values, the key:value pairs
#You can use two variables to go through them

for aaa,bbb in testdic.items():
    print(aaa,bbb)




#You can use variable += 1 INSTEAD OF variable = variable + 1, NEAT!
#compact alternative for incrementing a variable. counts[word] += 1 is equivalent to counts[word] = counts[word] + 1.
#Either method can be used to change the value of a variable by any desired amount. Similar alternatives exist for -=, *=, and /=.
