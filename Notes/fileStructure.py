import yaml
import os

# ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┬

#inputFile = "buildStructure.yml"
#outputFile = "Build structure"
inputFile = "fileStructure.yml"
outputFile = "File structure"
sameFolder = True # Same as this file?

def examineComment(data, indent="", index=0):
    output = ""
    index = 1
    lastWasFile = False
        
    for item in data:
            
        output += indent + "║\n"

        if type(item) == dict:
            if lastWasFile:
                output += indent + "║\n"

            name = list(item.keys())[0]

            if index == len(data):
                output += indent + "╚═" + name + "\n"
                output += examineComment(item[name], indent + "    ", index)
            else:
                output += indent + "╠═" + name + "\n"
                output += examineComment(item[name], indent + "║   ", index)

            if index < len(data):
                output += indent + "║\n"

        else:

            lastWasFile = True

            if index == len(data):
                name = item.replace("\n", "\n" + indent + "  ")
                output += indent + "╚═" + name + "\n"
            else:
                name = item.replace("\n", "\n" + indent + "║ ")
                output += indent + "╠═" + name + "\n"
        index += 1
    return output



def examine(data, indent="", index=0):
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
        output += examine(data[name], indent + spaces)
    
    elif type(data) == list:
        
        for item in data:

            if type(item) == dict:
                if lastWasFile:
                    output += indent + "│\n"

                name = list(item.keys())[0]
                
                if "." in name:

                    if index == len(data):
                        output += indent + "└─" + name + "\n"
                        output += examineComment(item[name], indent + "    ", index)
                    else:
                        output += indent + "├─" + name + "\n"
                        output += examineComment(item[name], indent + "│   ", index)

                    if index < len(data):
                        output += indent + "│\n"

                else:
                    extraSpaces = ""
                    for i in range(len(name)):
                        extraSpaces += " "

                    if index == len(data):
                        output += indent + "└─" + name + "─┐" + "\n"
                        output += examine(item[name], indent + "   " + extraSpaces, index)
                    else:
                        output += indent + "├─" + name + "─┐" + "\n"
                        output += examine(item[name], indent + "│  " + extraSpaces, index)

                    if index < len(data):
                        output += indent + "│\n"

            else:

                lastWasFile = True

                if index == len(data):
                    name = item.replace("\n", "\n" + indent + "  ")
                    output += indent + "└" + name + "\n"
                else:
                    name = item.replace("\n", "\n" + indent + "│ ")
                    output += indent + "├" + name + "\n"
            index += 1
    return output

scriptFolder = ""
if sameFolder:
    scriptFolder = os.path.dirname(os.path.abspath(__file__)) + "/"
                                
with open(scriptFolder + inputFile, "r") as file:
    data = yaml.safe_load(file)
    #print(data)
    output = ""
    output = examine(data)
    print(output)

    with open(scriptFolder + outputFile, "w") as file:
        file.write(output)