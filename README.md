# norma-machine

#### Integrantes: Antonio Rafael, Arycia Cabral, Fábio Cypreste, Nélio Espíndula Junior, Paulo Rhyan Kuster

Este projeto tem como objetivo implementar uma máquina Norma capaz de realizar as operações de soma, multiplicação e cálculo de fatorial. A máquina possui 8 registradores cujos valores são inicializados pelo usuário.

A operação desejada é determinada pelo nome do arquivo que contém o algoritmo correspondente. Os nomes dos arquivos para esta máquina são os seguintes:

- sum.txt
- multiply.txt
- factorial.txt
- lesser.txt
- mod.txt
- prime.txt

Após selecionar a operação, o algoritmo é carregado e o usuário é solicitado a inserir os valores nos registradores.

Nosso código:

```py
registers = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}

def sub(registers, register):
    registers[register] -= 1

def sum(registers, register):
    registers[register] += 1

def zero(registers, register):
    return registers[register] == 0

instructions_dictionary = {"SUB": sub, "SUM": sum}

for key in registers:
    registers[key] = int(
        input("Insert value for %s (for zero values, let it empty or type 0): " % key)
        or 0
    )

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
```

##

### SOMA

A soma exige que seja inserido os valores a serem somados nos registradores A e B, os demais devem permanecer vazios.

O resultado é exibido no registrador `"A"`.

```
1: ZER B 5 2
2: SUM A 3
3: SUM C 4
4: SUB B 1
5: ZER C 100 6
6: SUM B 7
7: SUB C 5
```

### MULTIPLICAÇÃO

A multiplicação exige que seja inserido os valores a serem somados nos registradores A e B, os demais devem permanecer vazios.

O resultado é exibido no registrador `"A"`.

```
1: ZER A 4 2
2: SUM C 3
3: SUB A 1
4: ZER C 20 5
5: SUB C 6
6: ZER B 10 7
7: SUM A 8
8: SUM D 9
9: SUB B 6
10: ZER D 4 11
11: SUM B 12
12: SUB D 10
```

### FATORIAL

O fatorial exige que seja inserido o número a ser calculado apenas no registrador A, os demais devem permanecer vazios.

O resultado é exibido no registrador `"A"`.

```
1: ZER A 5 2
2: SUM C 3
3: SUM D 4
4: SUB A 1
5: ZER C 30 6
6: SUB C 7
7: ZER C 10 8
8: SUM B 9
9: SUB C 7
10: ZER D 16 11
11: SUB D 12
12: ZER B 7 13
13: SUM A 14
14: SUM C 15
15: SUB B 12
16: SUB B 17
17: ZER B 30 18
18: ZER B 21 19
19: SUM C 20
20: SUB B 18
21: ZER A 7 22
22: SUM D 23
23: SUB A 21
```

### MENOR QUE / MAIOR QUE

O comparativo menor que exige que seja inserido o valor no registrador A e o que vai ser comparado no registrador B, os demais devem permanecer vazios. O resultado pode ser exibido nos registradores `"C"`, `"D"` ou `"E"`:

- Se o registrador `"C"` for 1, A é igual à B.
- Se o registrador `"D"` for 1, A é maior do que B.
- Se o registrador `"E"` for 1, A é menor do que B.

```
1: ZER A 5 2
2: SUB A 3
3: ZER B 8 4
4: SUB B 1
5: ZER B 7 6
6: SUM E 100
7: SUM C 100
8: SUM D 100
```

### DIVISÃO INTEIRA

O método para dizer se o resto da divisão entre dois números é inteiro exige que seja inserido valores em A e B, os demais devem permanecer vazios. O resultado é exibido nos registradores `"H"` ou `"G"`:

- Se `"H"` for 1, é divisível e o resto é zero.
- Se `"G"` for 1, não é divisível.

```
1: ZER B 2 3
2: SUM H 21
3: ZER A 4 5
4: SUM G 21
5: ZER A 9 6
6: SUM C 7
7: SUM D 8
8: SUB A 5
9: ZER D 12 10
10: SUM A 11
11: SUB D 9
12: ZER C 20 13
13: ZER B 17 14
14: SUB C 15
15: SUB B 16
16: SUM D 12
17: ZER D 12 18
18: SUM B 19
19: SUB D 17
20: ZER B 2 4
21: ZER D 100 22
22: SUM B 23
23: SUB D 21
```

### PRIMO

Para determinar se o número é primo ou nao, é necessário atribuir o valor à ser verificado no registrador A, os demais devem permanecer vazios. O resultado é exibido nos registradores `"F"` e `"E"`, tal que:

- Se `"F"` for 1, o número é primo.
- Se `"E"` for 1, o número não é primo.

```
1: ZER A 2 3
2: SUM E 100
3: ZER A 7 4
4: SUB A 5
5: SUM B 6
6: SUM C 3
7: ZER B 10 8
8: SUM A 9
9: SUB B 7
10: SUB C 11
11: ZER C 12 13
12: SUM H 31
13: ZER A 14 15
14: SUM G 31
15: ZER A 19 16
16: SUM B 17
17: SUM D 18
18: SUB A 15
19: ZER D 22 20
20: SUM A 21
21: SUB D 19
22: ZER B 30 23
23: ZER C 27 24
24: SUB B 25
25: SUB C 26
26: SUM D 22
27: ZER D 22 28
28: SUM C 29
29: SUB D 27
30: ZER C 12 14
31: ZER D 34 32
32: SUM C 33
33: SUB D 31
34: ZER C 35 10
35: ZER H 38 36
36: SUB H 37
37: SUB H 38
38: ZER H 39 2
39: SUM F 100
```
