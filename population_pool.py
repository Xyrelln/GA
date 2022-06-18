import random
import fitness_functions
import chromosome

def generate_population(size):
    population = []
    for i in range(size):
        population.append(chromosome.individual())

    return population

def sort_population_by_fitness(population):
    return sorted(population, key=fitness_functions.apply_function)

def choice_by_roulette(population):
    offset = 0
    sorted_population = sort_population_by_fitness(population)
    fitness_sum = sum(fitness_functions.apply_function(individual) for individual in population)
    
    normalized_fitness_sum = fitness_sum
    lowest_fitness = fitness_functions.apply_function(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        fitness = fitness_functions.apply_function(individual) + offset
        probability = fitness / normalized_fitness_sum
        accumulated += probability

        if draw <= accumulated:
            return individual


def crossover(individual_a, individual_b):
    # individual_a_decimal_dna = fitness_functions.dna_to_number(individual_a)
    # individual_b_decimal_dna = fitness_functions.dna_to_number(individual_b)

    cut_point = random.randint(2, 11)
    new_dna = [individual_a.dna[i] for i in range(0, cut_point)] + [individual_b.dna[i] for i in range(cut_point, 12)]
    
    return chromosome.individual(dna=new_dna)


def mutate(individual, probability):
    luck = random.uniform(0, 1)

    if(luck < probability):
        mutation_index = random.randint(0,11)
        individual.dna[mutation_index] = 1 - individual.dna[mutation_index]

    return individual


def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)

    for i in range(population_size):
        first_choice = choice_by_roulette(sorted_by_fitness_population)
        second_choice = choice_by_roulette(sorted_by_fitness_population)

        individual = crossover(first_choice, second_choice)
        individual = mutate(individual, 0.1)
        next_generation.append(individual)

    return next_generation