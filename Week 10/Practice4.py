#Now to sort by VALUE instead of key, we can extract a dictionary and ut it in a tuple,
# and then sort the REVERSED version of that tuple
# Step by step:
d = {'a':10, 'b': 1, 'c':22}    #Create a dictionary called d
tmp = list()                    #Create a list called tmp
for k, v in d.items():          #for every (key, value) tuple in list of dictionary items
    tmp.append( (v, k) )        #add these tuple values to the list tmp, but as VALUE (v) and KEY (k) (so not key value but the other way around)
print(tmp)                      #print the list, this will show that values are now first and keys second
tmp = sorted(tmp, reverse=True) #make tmp a sorted version of tmp, but sorted in reverse order (high to low instead of low to high I believe)
print(tmp)                      #print list again
