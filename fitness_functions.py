import chromosome

def binary_to_decimal(dna):
    result = 0

    i = 0
    while i < len(dna):
        result += dna[-1 * i - 1] * 2**i
        i += 1
    
    return result

def dna_to_number(dna):
    converted_dna = []
    x = binary_to_decimal([dna[i] for i in range(0, 4)])
    y = binary_to_decimal([dna[i] for i in range(4, 8)])
    z = binary_to_decimal([dna[i] for i in range(8, 12)])
    converted_dna.append(x)
    converted_dna.append(y)
    converted_dna.append(z)

    return converted_dna

def target(individual):
    converted_dna = dna_to_number(individual.dna)
    x, y, z = converted_dna

    return (2* x**2 - 3* y**2 - 4* x + 5* y + z)

def apply_function(individual):
    converted_dna = dna_to_number(individual.dna)
    x, y, z = converted_dna

    return (2* x**2 - 3* y**2 - 4* x + 5* y + z)


