import random


boundaries = (0, 16)
generations = 100

def generate_population(size, x_boundaries, y_boundaries, z_boundaries):
    lower_x_boundary, upper_x_boundary = x_boundaries
    lower_y_boundary, upper_y_boundary = y_boundaries
    lower_z_boundary, upper_z_boundary = z_boundaries

    population = []
    for i in range(size):
        individual = {
            "x": random.randint(lower_x_boundary, upper_x_boundary),
            "y": random.randint(lower_y_boundary, upper_y_boundary),
            "z": random.randint(lower_z_boundary, upper_z_boundary),
        }
        population.append(individual)

    return population


def apply_function(individual):
    x = individual["x"]
    y = individual["y"]
    z = individual["z"]
    return (2* x**2 - 3* y**2 - 4* x + 5* y + z)


def choice_by_roulette(sorted_population, fitness_sum):
    offset = 0
    normalized_fitness_sum = fitness_sum

    lowest_fitness = apply_function(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        fitness = apply_function(individual) + offset
        probability = fitness / normalized_fitness_sum
        accumulated += probability

        if draw <= accumulated:
            return individual


def sort_population_by_fitness(population):
    return sorted(population, key=apply_function)


def crossover(individual_a, individual_b):
    xa = individual_a["x"]
    ya = individual_a["y"]
    za = individual_a["z"]

    xb = individual_b["x"]
    yb = individual_b["y"]
    zb = individual_b["z"]

    return {"x": (xa + xb) / 2, "y": (ya + yb) / 2, "z": (za + zb) / 2}


def mutate(individual):
    next_x = individual["x"] + random.uniform(-0.05, 0.05)
    next_y = individual["y"] + random.uniform(-0.05, 0.05)
    next_z = individual["z"] + random.uniform(-0.05, 0.05)

    lower_boundary, upper_boundary = (0, 16)

    # Guarantee we keep inside boundaries
    next_x = min(max(next_x, lower_boundary), upper_boundary)
    next_y = min(max(next_y, lower_boundary), upper_boundary)
    next_z = min(max(next_z, lower_boundary), upper_boundary)
    return {"x": next_x, "y": next_y, "z": next_z}


def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)
    fitness_sum = sum(apply_function(individual) for individual in population)

    for i in range(population_size):
        first_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)
        second_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)

        individual = crossover(first_choice, second_choice)
        individual = mutate(individual)
        next_generation.append(individual)

    return next_generation

import matplotlib.pyplot as plt

population = generate_population(size=100, x_boundaries=boundaries, y_boundaries=boundaries, z_boundaries=boundaries)

i = 1
best_of_generation = []
while True:
    # print(f"🧬 GENERATION {i}")

    # for individual in population:
    #    print(individual, apply_function(individual))
    best_individual_of_generation = sort_population_by_fitness(population)[-1]
    best_of_generation.append(apply_function(best_individual_of_generation))
    if i >= generations:
        break

    i += 1

    population = make_next_generation(population)

xpoints = range(100)
plt.plot(xpoints, best_of_generation)
plt.show()

best_individual = sort_population_by_fitness(population)[-1]
print("\n🔬 FINAL RESULT")
print(best_individual, apply_function(best_individual))    