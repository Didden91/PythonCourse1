def count(letter, word):
    counter = 0
    for search in word:
        if search == letter:
            counter = counter + 1
    return counter

letterinput = input("Enter a letter: ")
wordinput = input("Enter a word: ")
wordinput = wordinput.strip('b ')


counter = count(letterinput, wordinput)
print(counter)

lowercasewordinput = wordinput.lower()

if lowercasewordinput < 'banana':
    print("Your word:",wordinput,"comes before banana")
elif lowercasewordinput > 'banana':
    print("Your word:",wordinput,"comes after banana")
else:
    print("Well everything is just bananas")

print("What I actually checked was",lowercasewordinput)
