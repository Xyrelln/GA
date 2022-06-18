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

def choice_by_roulette(population, mode=max):
    offset = 0
    fitness_sum = 0

    if mode == max:
        for individual in population:
            fitness = fitness_functions.apply_function(individual)
            fitness_sum += fitness
            if fitness < offset:
                offset = fitness
    else:
        for individual in population:
            fitness = -1 * fitness_functions.apply_function(individual)
            fitness_sum += fitness
            if fitness < offset:
                offset = fitness

    fitness_sum += -1 * offset * len(population)

    roulette = []
    sum_proportion = 0
    if mode == max:
        for individual in population:
            proportion = (fitness_functions.apply_function(individual) - offset) / fitness_sum
            sum_proportion += proportion
            roulette.append(sum_proportion)
    else:
        for individual in population:
            proportion = (-1 * fitness_functions.apply_function(individual) - offset) / fitness_sum
            sum_proportion += proportion
            roulette.append(sum_proportion)
    
    draw = random.uniform(0, 1)

    for index in range(len(population)):
        if draw < roulette[index]:
            return population[index]



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


def make_next_generation(previous_population, mode=max):
    next_generation = []
    # sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)

    if mode == max:
        for i in range(population_size):
            first_choice = choice_by_roulette(previous_population, mode=max)
            second_choice = choice_by_roulette(previous_population, mode=max)

            individual = crossover(first_choice, second_choice)
            individual = mutate(individual, 0.1)
            next_generation.append(individual)
    else:
        for i in range(population_size):
            first_choice = choice_by_roulette(previous_population, mode=min)
            second_choice = choice_by_roulette(previous_population, mode=min)

            individual = crossover(first_choice, second_choice)
            individual = mutate(individual, 0.1)
            next_generation.append(individual)

    return next_generation