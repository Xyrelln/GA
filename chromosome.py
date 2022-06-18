import random


class individual:
    dna = random.choices(range(2), k=12)

    def __init__(chromosome, dna=None):
        if dna:
            chromosome.dna = dna
        else:
            chromosome.dna = random.choices(range(2), k=12)
