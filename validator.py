import xml.etree.ElementTree as ET
import os

def validate_text_file(file_path, error_list, error_counts):
    with open(file_path, 'r') as file:
        file_name = os.path.basename(file_path)
        print(f"{file_name = }")
        if file_name not in error_counts:
            error_counts[file_name] = {'errors': 0, 'warnings': 0, 'info': 0}
        print(f"{error_counts = }")
        #error_counts[file_name]['warnings'] = 0
        #error_counts[file_name]['info'] = 0

        lines = file.readlines()
        for line_num, line in enumerate(lines, start=1):
            if 'ERROR' in line:
                error_info = {
                    'error_description': 'Line contains ERROR',
                    'line_number': line_num,
                    'line_content': line.strip(),
                    'file_name': file_name
                }
                error_list.append(error_info)
                error_counts[file_name]['status'] = 'Error'
                error_counts[file_name]['errors'] += 1
            elif 'WARNING' in line:
                error_counts[file_name]['warnings'] += 1
            elif 'INFO' in line:
                error_counts[file_name]['info'] += 1

        print(f"{error_counts[file_name]['errors'] = }")
        
## fileds
# different X and Free Format
# date with format
# int with format

## code
# empty line for begin end else if
# only one empty line
# cerror() not in code
# comma around , . = & ....
# double space
# check for break
# check for more then one ;
# check indentation
# check if variable are use
# check variable name
# check if do and then are in same line
# check function are lowercase
# java
# check while


def validate_xml_file(file_path, error_list, error_counts):
    tree = ET.parse(file_path)
    root = tree.getroot()
    if len(root) > 5:
        error_info = {
            'rule_number': 1,
            'rule_content': 'XML has more than 5 children',
            'error_description': 'XML validation failed',
        }
        error_list.append(error_info)
        error_counts[file_path]['errors'] += 1
## General


## MapSettings
# MapAudit is not set to 'off'
# MapTrace is not set to 'off'

## MapInput

## MapOutput
#+ MapRule
# check for function that cannot be use
# check if unction is not uppercase

def validate_file(file_path, error_list, error_counts):
    if file_path.endswith('.txt'):
        validate_text_file(file_path, error_list, error_counts)
    elif file_path.endswith('.xml'):
        validate_xml_file(file_path, error_list, error_counts)
    else:
        raise ValueError("Unsupported file format.")


def export_errors(error_list, file_path):
    with open(file_path, 'w') as file:
        for error in error_list:
            file.write(str(error) + "\n")

