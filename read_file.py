import re

def read_file():
    file = None
    operations = list()

    while file is None:
        file_name = input("Enter the file name inside this directory: ")
        
        try:
           with open(file_name, 'rt') as search_file:
                for line in search_file:
                    operation = re.findall(r'(\w+)\s+(\w+)\s+(\d+)\s*(\d+)*$', line, flags=re.M |re.I)
                    if operation:
                        operations.append(list(operation[0]))
        except (FileNotFoundError):
            print("File not found. Please try again.")
        else:
            file = search_file
            return operations
    
    print(file.read())