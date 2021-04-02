inpname = input('please enter a file name: ')
fileoutput = open(inpname,'w')

textinp = input('Write something to put in the file: ')
fileoutput.write(textinp)
fileoutput.write('\n')

while True:
    cont = input('Do you want to input another line? ')

    if cont == 'y' or cont == 'Y':
        textinp = input('Write something to put in the file: ')
        fileoutput.write(textinp)
        fileoutput.write('\n')
    else:
        fileoutput.close()
        quit()
