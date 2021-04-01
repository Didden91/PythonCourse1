text = "X-DSPAM-Confidence:    0.8475"
strlength = len(text)
colonpos = text.find(':')
print(colonpos)
print(strlength)
data = text[colonpos+1:strlength]
data = float(data)
print(data)


#endpos = str.find(' ',colonpos)
#print(endpos)
