def print_instruction(operation):
    if operation[0] == "ZER":
        return "SE ZER (%s) ENTÃO VÁ PARA %s. SE NÃO, VÁ PARA %s." % (operation[1], operation[2], operation[3])
    else:
        return "FAÇA %s (%s) VÁ PARA %s." % (operation[0], operation[1], operation[2])