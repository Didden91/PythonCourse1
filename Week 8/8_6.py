total = list()
while True:
    numbinp = input("enter a number:")
    if numbinp == 'done': break
    floatnum = float(numbinp)
    total.append(floatnum)
print("Maximum:",max(total))
print("Minimum:",min(total))
