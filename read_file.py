import os

keyWords = ('begin', 'end')

def read_text_file(filePath, filesContent):
    with open(filePath, 'r') as file:
        fileName = os.path.basename(filePath)
        if fileName not in filesContent:
            filesContent[fileName] =  {'GeneralSection': 'missing', 
                                        'BranchInput': 'missing',
                                        'BranchOutput': 'missing',
                                        'FieldsInput': 'missing',
                                        'FieldsOutput': 'missing',
                                        'CodeSection': 'missing',
                                        'CodeLists': 'missing'}
        lines = file.readlines()
        currentSection = ""
        for lineNum, line in enumerate(lines, start=1):
            if line.endswith('\n'):
                line = line[:-1]
            lineTrim = line.strip()
            if lineTrim == "General Section":
                currentSection = "GeneralSection"
                if filesContent[fileName][currentSection] == 'missing':
                    filesContent[fileName][currentSection] = 'empty'
            elif lineTrim == "Branch Input":
                currentSection = "BranchInput"
                if filesContent[fileName][currentSection] == 'missing':
                    filesContent[fileName][currentSection] = 'empty'
            elif lineTrim == "Branch Output":
                currentSection = "BranchOutput"
                if filesContent[fileName][currentSection] == 'missing':
                    filesContent[fileName][currentSection] = 'empty'
            elif lineTrim == "Fields Input":
                currentSection = "FieldsInput"
                if filesContent[fileName][currentSection] == 'missing':
                    filesContent[fileName][currentSection] = 'empty'
            elif lineTrim == "Fields Output":
                currentSection = "FieldsOutput"
                if filesContent[fileName][currentSection] == 'missing':
                    filesContent[fileName][currentSection] = 'empty'
            elif lineTrim == "Code Section":
                currentSection = "CodeSection"
                fieldName = ""
                if filesContent[fileName][currentSection] == 'missing':
                    filesContent[fileName][currentSection] = 'empty'
            elif lineTrim == "Code Lists":
                currentSection = "CodeLists"
                if filesContent[fileName][currentSection] == 'missing':
                    filesContent[fileName][currentSection] = 'empty'
            else:
                print(f"{currentSection = }")
                if currentSection == "CodeSection":
                    print(f"{line = }")
                    if len(line) >= 3 and line[2] != " " and "------" not in line and ";" not in line and line not in keyWords:
                        fieldName = lineTrim
                        print(f"{fieldName = }")
                    else:
                        print(f"else - {fieldName = }")
                        if fieldName != '':
                            if filesContent[fileName][currentSection] == 'empty':
                                filesContent[fileName][currentSection] = {}
                            print(f"{filesContent[fileName][currentSection] = }")
                            if fieldName not in filesContent[fileName][currentSection]:
                                print(f"{filesContent[fileName][currentSection] = }")
                                filesContent[fileName][currentSection][fieldName] = [] 
                            filesContent[fileName][currentSection][fieldName].append({
                                'lineInPTF': lineNum,
                                'line': line,
                                'lineTrim': lineTrim
                            })
                    print(f"{filesContent = }")
                elif currentSection != "":
                    if filesContent[fileName][currentSection] == 'empty':
                        filesContent[fileName][currentSection] = []
                    filesContent[fileName][currentSection].append({
                        'lineInPTF': lineNum,
                        'line': line
                    })

def read_xml_file(file_path, file_content):
    tree = ET.parse(file_path)
    root = tree.getroot()


def read_file(file_path, file_content):
    if file_path.endswith('.txt'):
        read_text_file(file_path, file_content)
    elif file_path.endswith('.xml'):
        read_xml_file(file_path, file_content)
    else:
        raise ValueError("Unsupported file format.")
