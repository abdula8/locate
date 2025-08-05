from locate import search, help
from sys import argv
from os import system

# Clear window before printing results
system("cls")

# applying searching function by getting first argument from cmd
charCase=str(argv[1]).lower()
if (charCase == '-f') or (charCase == '-fc') or (charCase == '-cf'):
    search(searchFileName=str(argv[3]), searchPattern=str(argv[2]), charCase=charCase)
elif (charCase == '--help') or (charCase == '-h'):
    help()
else:
    search(searchFileName=str(argv[2]), searchPattern=None, charCase=str(argv[1]))

print('''
What do want to do next ?
        COPY(c)
        DELETE(d)
        CUT(ct)
        
''')
