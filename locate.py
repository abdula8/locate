

# To use this script here ia an example:
# write ==> python script_name.py SEARCH-WORD DIRECTORY-TO-SEARCH-ON SEARCH-FILE-TYPE
# SEARCH-FILE-TYPE if you want to search on all file types you can write "all" like:
# python search_on_disk.py NAME d: all
# if you want to search directories write in file type "dir" like this
# python search_on_disk.py NAME d: dir
#new update idea AT 202226102005WED
#locate NAME
#script will be converted to .bat file then 
'''
    .bat file script
    the arguments passed to bat file 
    there is no need to write python search_on_disk NAME D: all
    now it will be python search_on_disk NAME D:
            then it will search for all file types and print the path of it if it was found
    in the future it will be just: "locate FILENAME"

'''

# Update on code at 2022-08-31:18:04
'''
from
>>
if new_file_name.endswith("mp4") and file_type == "videos":
    find_file(search_name, new_file_name, folderName, filename)
TO
>>
if new_file_name.endswith(file_type):
    find_file(search_name, new_file_name, folderName, filename)



'''



import os
import sys
from datetime import datetime

folder_names_backup = {}
print("\n\n\n")
search_directory = str(sys.argv[2])
os.chdir(search_directory)
print(os.getcwd())
resultsList = []

def find_file(search_name, new_file_name, folderName, filename):
    if search_name in new_file_name:
        results = search_directory+"\\"+ folderName + "\\" + filename # datetime added 202208141240 --> 202226102017
        # print("search result: file found in ")
        # print("\n\t\t",folderName,"\n", filename,"\n")
        print(results)
        resultsList.append(results)


def search(search_name):
    current_folder_count = 0
    # subfolder_count = 0
    files_count = 0
    for folderName, subfolders, filenames in os.walk(search_directory):
        # print('The current folder is ' + folderName)
        current_folder_count += 1
        folder_names_backup[folderName] = subfolders + filenames
        for filename in filenames:
            # print('FILE INSIDE ' + folderName + ': '+ filename)
            files_count += 1
            new_file_name = filename.lower()
            find_file(search_name, new_file_name, folderName, filename)


# Clear window before printing results
os.system("cls")

# applying searching function by getting first argument from cmd
search(str(sys.argv[1]))

# store results in a file with the name of searching word in the searching directory
# NOW: it is deactivated which you c an redirect the output using the --> python locate NAME d: > STORENAME
'''
resultFileName = str(sys.argv[1]) + datetime.now().strftime("%Y%m%d%I%M%S%p")
with open(search_directory+'\\'+resultFileName, 'w+') as file:
    for i in resultsList:
        file.write(i)
'''


# print("Number of files = {}\n, Number of directories = {}\n, Numner of sub directories = {}\n".format(fc, cfc, sfc))
# print("\n",int(files_count))
