import csv

csv.register_dialect('forCSV', delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\', lineterminator='\n')

def writeFile(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)

def writeCSV(content, file_name, columns=[]):
    # if is a dictionary, convert to list
    if isinstance(content, dict):
        new_content = [columns]
        for item in content:
            new_content.append([item, content[item]])
        content = new_content
    # wrist CSV
    with open(file_name, 'w') as file:
        writer = csv.writer(file, dialect='forCSV')
        writer.writerows(content)
