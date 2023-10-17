#Asks the user for an input in camel case
C = input("camelCase: ")
#Checks every letter in the code individually
for i in range(len(C)):
    #Checks if the letter is uppercase
    if C[i].isupper() == True:
        #If it is uppercase print a '_' before the letter
        print('_',C[i].lower(),end="",sep="")
    else:
        #If it is lowercase just print the letter and move on
        print(C[i],end="",sep="")
