#Introduces new functionality
import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
#Contains all of the fonts from figlet
l = figlet.getFonts()
#If the length of the input in the command line is 3 and it starts with '-f' or '--font' then it will...
if len(sys.argv) == 3 and sys.argv[1]=='-f' or len(sys.argv) == 3 and sys.argv[1]=='--font':
    #Save the next word as 'font'
    figlet.setFont(font=sys.argv[2])
    #The user will be asked for an input
    i = input("Input: ")
    #The input will be turned into the font that they entered and printed
    print("Output:",figlet.renderText(i))
#If the command line input is nothing then...
elif len(sys.argv) < 2:
    #A random font from figlet will be chosen
    random.choice(l)
    #The user will be asked for an input
    n = input("Input: ")
    #The input will be printed once again but in a random font
    print("Output:",figlet.renderText(n))
#If the command line input doesn't meet either requirement then it will print 'Invalid usage'
else:
    sys.exit("Invalid usage")

