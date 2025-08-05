'''
There are 3 functions:
    find_file():
        this function is implementing the searching conditions
        depending on arguments passed from the user
        -c      to search the exact file name case sensetivity
        -f      to search about string in a the files with specific name or its name contains some string
        -fc     to search in file about string but the file name must be same as in disk case sensetive
        -non    to search about file that contains in its name some string.

'''

from os import walk, chdir, getcwd
from sys import argv
from datetime import datetime

# folder_names_backup = {}
# print("\n\n\n")

search_directory = str(argv[-1])

def find_file(searchFileName:str, searchPattern:str, fileName:str, folderName:str, filename:str, charCase:str) -> None:
    '''
    This function just implement the if condition for checking the file name
    the grep here is used to search a pattern in all files with the searchFileName parameter

    using folderName.split(':')[1] instead of folderName 
    because using folderName print incorrect path e.g. e:dir\
    and correct is e:\dir\ so i used search_directory variable
    and split function with folderName variable with this dilimeter ':' 
    '''
    if (charCase == '-h') or (charCase == '--help'):
        help()
    elif (charCase == '-c'):
        exactFileName(searchFileName, fileName, folderName, filename)
    elif charCase == '-f':
        from grep import grep
        grepFileName = search_directory+"\\"+ folderName.split(':')[1] + "\\" + filename
        grep(searchPattern, grepFileName)
    elif charCase == '-cf' or charCase == '-fc':
        from grep import grep
        grepFileName = exactFileName(searchFileName, fileName, folderName, filename)
        grep(searchPattern, grepFileName)
        if grepFileName:
            print(grepFileName)
    # search usnign regex
    elif charCase == '-r':
        import re
        # Convert the user's wildcard pattern into a valid regular expression
        # '*' becomes '.*' (match any character, zero or more times)
        # '.' is escaped to match a literal dot
        regex_pattern = searchFileName.replace('.', r'\.').replace('*', '.*')
        # 'searchFileName' is the regex pattern, 'search_directory' is the root,
        # 'folderName' is the current folder, and 'filename' is the file.
        reg = re.compile(regex_pattern, re.IGNORECASE) # Use re.IGNORECASE for true case-insensitivity
        
        # Construct the full path using os.path.join for cross-platform compatibility
        # and avoiding the brittle split() logic.
        from os import path
        full_path = path.join(search_directory, folderName, filename)
        
        if reg.search(filename):
            print(f"Found match: {full_path}")

    elif charCase == '-non':
        if searchFileName in fileName.lower():
            # result = search_directory+"\\"+ folderName.split(':')[1] + "\\" + filename
            from os import path
            full_path = path.join(search_directory, folderName, filename)
            print(f"Found match: {full_path}")
            # print(result)
            # resultsList.append(result)
    else:
        print("See locate --help or locate -h, to see how use the command.")


# this function is used to get the file with the exact matching name
def exactFileName(searchFileName:str, fileName:str, folderName:str, filename:str) -> None:
    """
    This function just implement the if condition for checking the file name
    fileName if the filename.lower()
    """
    if (searchFileName == fileName):
        # if :
        result = search_directory+"\\"+ folderName.split(':')[1] + "\\" + filename
        print("File found in : \n \t", result)
        # resultsList.append(result)
        return result

def help():
    print('''
        NAME:
          locate - list files in the disk that contain or match some string
        locate -non to search file that contains in its name string you specified
               -c   get file with specific name case sensetive
               -f   get string from files 
               -fc  get string from specific file(s)
               -r   search using regex patterns in python
               -h or --help display this list
            ''')

def search(searchFileName:str, searchPattern:str, charCase:str) -> list:
    '''
    This is the main function for searching for the file in the hard disk
    
    '''
    current_folder_count = 0
    # subfolder_count = 0
    files_count = 0
    for folderName, subfolders, filenames in walk(search_directory):
        current_folder_count += 1
        # folder_names_backup[folderName] = subfolders + filenames
        for filename in filenames:
            files_count += 1
            find_file(searchFileName, searchPattern, filename, folderName, filename, charCase)
