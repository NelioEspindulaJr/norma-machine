from operations.sub import sub
from operations.sum import sum
from operations.zero import zero

from read_file import read_file

registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}

instructions_dictionary = {'SUB': sub, 'SUM': sum}

operations = read_file()

if len(operations) == 0:
    print("No operations found.")
    exit()

print(operations)

for key in registers:
    registers[key] = int(input('Insert value for %s (for zero values, let it empty or type 0): ' % key) or 0)

operation_index_identifier = 0

while operation_index_identifier <= len(operations):
    operation = operations[operation_index_identifier]

    print("operation", operation)

    if operation[0] == "ZER":
       if zero(registers, operation[1]) == True:
           operation_index_identifier = int(operation[2]) - 1
       else:
           operation_index_identifier = int(operation[3]) - 1 
    else:
       instructions_dictionary[operation[0]](registers, operation[1])
       operation_index_identifier = int(operation[2])- 1

print(registers)
