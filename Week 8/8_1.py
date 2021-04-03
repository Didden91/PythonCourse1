def chop(linp):
    del linp[0]
    del linp[len(linp)-1]

def middle(linp):
    return linp[1:len(linp)-1]



lijstje = ['apple', 'banana', 'pear', 'pineapple' , 'grape']
lijstje2 = ['apple', 'banana', 'pear', 'pineapple' , 'grape']
print(lijstje)

chop(lijstje)
print(lijstje)

print('en nu lijst twee')
print(lijstje2)

newlijst2 = middle(lijstje2)
print(newlijst2)

print(lijstje)
print(lijstje2)
