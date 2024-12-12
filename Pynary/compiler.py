import os, runpy
from colorama import Fore, Style

os.system('clear')
setf = open("/workspaces/codespaces-blank/.vscode/scripts/set.txt", 'r')

setList = setf.read().splitlines()

setf.close()
# remove '\n' from the variables

# file input handling
while True:
    direct = setList[0]
    extend = setList[1]

    # current directory
    print("Current Directory: " + direct)

    file_name = input("File Name: ")
    tip = "Make sure you have no errors in your file name"

    # change directory
    if (file_name == "chdir"):
        idir = input("Directory: ")

        # always have a '/' at the end of directory
        if (idir[-1] != '/'):
            idir += '/'

        setList[0] = idir
        setf = open("/workspaces/codespaces-blank/.vscode/scripts/set.txt", 'w')

        # write to file
        for elem in setList:
            setf.write(elem + "\n")

        setf.close()
        os.system('clear')
    
    # change file extension
    elif (file_name == "chext"):
        iext = input("Extension: ")
        setList[1] = iext
        setf = open("/workspaces/codespaces-blank/.vscode/scripts/set.txt", 'w')

        # write to file
        for elem in setList:
            setf.write(elem + "\n")
        
        setf.close()
        os.system('clear')
    
    # fix file_name
    else:
        # no file extender
        if ('.' not in file_name):
            file_name += "." + extend

        else:
            index = file_name.index('.') + 1
            txt = ""

            # wrong file extender
            if (index != len(file_name)):
                while index < len(file_name):
                    txt += file_name[index]
                    index += 1

                # replace wrong file extender
                if (len(txt) > 0):
                    file_name = file_name.replace(txt, extend)

            # add txt
            else:
                file_name += extend

        # check handler
        try:
            if (file_name in os.listdir(direct)):
                os.system('clear')
                break
            else:
                # wrong file extender
                for dir in os.listdir(direct):
                    if (file_name.replace("." + extend, "") in dir):
                        tip = "Make sure you have a .pb file or verify directory"
        except:
            pass
        
        os.system('clear')
        # file not found
        print(Fore.RED + Style.BRIGHT + file_name + Style.RESET_ALL + " is not in " + Fore.YELLOW + Style.BRIGHT + direct + Fore.GREEN + Style.BRIGHT + "\nTip: " + Fore.WHITE  + tip + Style.RESET_ALL)
    # end

        # make sure to not duplicated binary.py
        try:
            os.remove("/workspaces/codespaces-blank/.vscode/scripts/binary.py")
        except:
            pass
        # end

# actual code :)
# variables
bitArr = []

# read program
f = open(str(direct + file_name), 'r')

# ignore comments
for line in f.readlines():
    if ('*' in line):
        continue
    else:
        # string to int
        try:
            bitArr.append(line)
        except:
            print("Error (Failed): Str -> Int") #str to int failed
            exit()

f.close()

# remove \n
for elem in bitArr:
    if ("\n" in elem):
        elemN = elem.strip()
        bitArr[bitArr.index(elem)] = elemN

# empty space error
for i in bitArr:
    if (' ' in i or len(i) == 0):
        print("Error: Empty space")
        exit()

def binToChar(list):
    letArr = []
    for elem in list:
        asc = int(elem, 2)
        letArr.append(chr(asc))

    # write to python file
    f = open('/workspaces/codespaces-blank/.vscode/scripts/binary.py', 'w')
    for elem in letArr:
        if (elem == "@"):
            f.write("\n")
        else:
            f.write(elem)
    
    f.close()

# function
binToChar(bitArr)

# run .py file
runpy.run_path(path_name='/workspaces/codespaces-blank/.vscode/scripts/binary.py')

# remove .py file
os.remove("/workspaces/codespaces-blank/.vscode/scripts/binary.py")
