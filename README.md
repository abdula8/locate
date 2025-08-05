# Locate Command for windows
This is the locate command like in the linux you can use in windows.
It is written in python and to run it you can create batch file as specified:
and put it in the c:\locate or directly in C: partition

## Installation
Installation steps:
1. Clone the [https:github.com/abdula8/locate.git](https://github.com/abdula8/locate.git)
2. Install python
### the exe file is comming soon
3. Add the path of the batch file in the PATH environmental variable to be able to access the command using command ine over the system
#### it is better to put c:\locate

## Usage
locate -non "file namE" path/of/search
e.g. locate -non python c: <== this will search any file contain in its name the word python without case sensetivety <what if you want to search about specific file name!!!>

locate -c "file name" path/of/search
e.g. locate -c "security CV.pdf" g:
this will search for the file with exact name "security CV.pdf" with case sensetivity 

locate -f "search pattern" "search file" path/of/file
e.g. locate -f security devops g: <== this will search inside anyfile about any line contains the word "security" and which the file name contains the word devops works for all files <but what if you want to search inside specific file!!!>

locate -fc "search pattern" "search file" path/of/file
locate -cf "search pattern" "search file" path/of/file
e.g. locate -fc security devopsLearn.txt g:
search about word "security" inside specific file named devopsLearn.txt with case sensetivity 

locate -r \<REGEX\> \<DIR\>
e.g. -> locate -r \*python\*.pdf d:

locate -h; or locate --help
to display the help list 

# EXE file is coming soon
