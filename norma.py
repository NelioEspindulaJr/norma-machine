from operations.sub import sub
from operations.sum import sum
from operations.zero import zero

from read_file import read_file
from print_instruction import print_instruction

registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}

instructions_dictionary = {"SUB": sub, "SUM": sum}

operations = read_file()

if len(operations) == 0:
    print("No operations found.")
    exit()

print(operations)

for key in registers:
    registers[key] = int(
        input("Insert value for %s (for zero values, let it empty or type 0): " % key)
        or 0
    )

print(
    "(%s, %s, %s, %s, %s, %s, %s, %s), M"
    % (
        registers["A"],
        registers["B"],
        registers["C"],
        registers["D"],
        registers["E"],
        registers["F"],
        registers["G"],
        registers["H"],
    )
)

operation_index_identifier = 0
index = 1

while operation_index_identifier < len(operations):
    operation = operations[operation_index_identifier]

    if operation[0] == "ZER":
        if zero(registers, operation[1]):
            operation_index_identifier = int(operation[2]) - 1
        else:
            operation_index_identifier = int(operation[3]) - 1
    else:
        instructions_dictionary[operation[0]](registers, operation[1])
        operation_index_identifier = int(operation[2]) - 1

    formatted_operation = print_instruction(operation)
    print(
        "(%s, %s, %s, %s, %s, %s, %s, %s), %s)    %s"
        % (
            registers["A"],
            registers["B"],
            registers["C"],
            registers["D"],
            registers["E"],
            registers["F"],
            registers["G"],
            registers["H"],
            index,
            formatted_operation,
        )
    )
    index += 1

print(registers)
