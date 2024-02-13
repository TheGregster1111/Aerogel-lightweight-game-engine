import yaml
import os
from colorama import Fore, Style

# ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴

# ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩

#         ╘ ╛ ╞ ╡ ╥ ╨

#inputFile = "buildStructure.yml"
#outputFile = "Build structure"
inputOutputFolder = "/home/susanne/source/repos/C++/Aerogel/"
inputFile = "fileStructure.yml"
#inputFile = "test.yml"
outputFile = "fileStructure.fsys"
sameFolder = True # Same as this file? If True no need to use inputOutputFolder

rootFolderLocation = "/home/susanne/source/repos/C++/Testing/"
mode = 1
# 0: Just print result
# 1: Generate text into output file
# 2: Generate folders and files
useColours = True
useExtension = True # Use with vs code extension made to display colour and add collapsible regions?

colourMarkers = ["", ""]
if useColours:
    if useExtension:
        colourMarkers = ["​", "‌"]
    else:
        colourMarkers = [Fore.GREEN, Style.RESET_ALL]

foldMarkers = ["", ""]
""" if useExtension:
    foldMarkers = ["{f}", "{/f}"] """

def examineComment(data, indent="", isLast=False, nested=False):
    output = ""
    index = 1
    lastWasFile = False

    if nested:
        boxSymbols = ["║", "╚═", "╠═"]
    else:
        boxSymbols = ["│", "╘═", "╞═"]
        
    for item in data:
        if index > 1:
            output += indent + colourMarkers[0] + boxSymbols[0] + colourMarkers[1] + "\n"

        if type(item) == dict:
            if lastWasFile:
                output += indent + colourMarkers[0] + boxSymbols[0] + colourMarkers[1] + "\n"

            name = list(item.keys())[0]

            extraSpaces = ""
            for i in range(len(name) + 2):
                extraSpaces += " "

            if index == len(data) and (isLast or nested):
                output += indent + colourMarkers[0] + boxSymbols[1] + "╡" + name + "╞═╗" + colourMarkers[1] + "\n"
                output += examineComment(item[name], indent + "   " + extraSpaces, isLast, True)
            else:
                output += indent + colourMarkers[0] + boxSymbols[2] + "╡" + name + "╞═╗" + colourMarkers[1] + "\n"
                output += examineComment(item[name], indent + colourMarkers[0] + boxSymbols[0] + "  " + extraSpaces + colourMarkers[1], isLast, True)

            if index < len(data):
                output += indent + colourMarkers[0] + boxSymbols[0] + colourMarkers[1] + "\n"

        else:

            lastWasFile = True

            if index == len(data) and (isLast or nested):
                name = item.replace("\n", colourMarkers[1] + "\n" + indent + colourMarkers[0] + "   # ") + colourMarkers[1]
                output += indent + colourMarkers[0] + boxSymbols[1] + " # " + name + "\n" 
            else:
                name = item.replace("\n", colourMarkers[1] + "\n" + indent + colourMarkers[0] + boxSymbols[0] + "  # ") + colourMarkers[1]
                output += indent + colourMarkers[0] + boxSymbols[2] + " # " + name + "\n"
        index += 1

    return output



def examine(data, indent="", fileComment=False, layer=0):
    output = ""
    index = 1
    lastWasFile = False
    if type(data) == dict: #Must be root folder
        name = list(data.keys())[0]
        spaces = " "
        for i in range(len(name)):
            spaces += " "
            
        output += indent + name + "─┐\n"
        #output += indent + spaces + "│\n"
        output += examine(data[name], indent + spaces, layer=1)
    
    if type(data) == list:
        for item in data:
            if type(item) == list: # Directory
                if lastWasFile:
                    output += indent + "│\n"

                #print(item)
                name = list(item[0].keys())[0]
                #print(name)

                extraSpaces = ""
                for i in range(len(name)):
                    extraSpaces += " "

                if index == len(data):
                    output += foldMarkers[0] + indent + "└─" + name + "─┐\n"
                    output += examine(item[0][name], indent + "   " + extraSpaces, layer=layer+1)
                else:
                    output += foldMarkers[0] + indent + "├─" + name + "─┐\n"
                    output += examine(item[0][name], indent + "│  " + extraSpaces, layer=layer+1)

                if index < len(data):
                    output += indent + "│\n"

                index += 1
                lastWasFile = False

                continue                

            elif type(item) == dict:

                name = list(item.keys())[0]
                
                if name == "<COMMENT>":

                    if fileComment:

                        output += indent + "│\n"

                    #output += indent + str(index) + "\n"

                    if index == len(data):
                        output += examineComment(item[name], indent, True)
                    else:
                        output += examineComment(item[name], indent, False)
                        output += indent + "│\n"

                else: # File

                    extraSpaces = ""
                    for i in range(len(name)):
                        extraSpaces += " "

                    if index == len(data):
                        output += indent + "└" + name + "\n"
                        output += examine(item[name], indent + "   ", True, layer=layer+1)
                    else:
                        output += indent + "├" + name + "\n"
                        output += examine(item[name], indent + "│  ", True, layer=layer+1)

                    if index < len(data):
                        output += indent + "│\n"

                index += 1
                lastWasFile = False
                continue
            
            # File

            lastWasFile = True

            if index == len(data):
                output += indent + "└" + item + "\n"
                output += indent + "\n"
            else:
                output += indent + "├" + item + "\n"
            index += 1

    return output

#Work in progress
def generate(data, path=""):
    output = ""
    index = 1
    lastWasFile = False
    if type(data) == dict: #Must be root folder
        name = list(data.keys())[0]
        if not os.path.exists(path + name):
            os.mkdir(path + name)

        examine(data[name], path + name + "/")
    
    elif type(data) == list:
        
        for item in data:

            if type(item) == dict:
                name = list(item.keys())[0]
                if not os.path.exists(path + name):
                    os.mkdir(path + name)

                if not "." in name:

                    examine(item[name], path + name + "/")

            else:
                name = list(item.keys())[0]
                if not os.path.exists(path + name):
                    os.mkdir(path + name)
                    with open(path + name, 'w') as file:
                        file.write('')

            index += 1
    return output

if sameFolder:
    inputOutputFolder = os.path.dirname(os.path.abspath(__file__)) + "/"
                                
with open(inputOutputFolder + inputFile, "r") as file1:
    data = yaml.safe_load(file1)

    if mode < 2:
        output = ""
        output = examine(data)
        print(output)

        if mode == 1:
            with open(inputOutputFolder + outputFile, "w") as file2:
                file2.write(output)