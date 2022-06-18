import random
import matplotlib.pyplot as plt
import chromosome, fitness_functions, population_pool


boundaries = (0, 15)
generations = 100

population = population_pool.generate_population(size=100)

i = 1
max_of_generation = []
min_of_generation = []
while True:
    max_individual_of_generation = population_pool.sort_population_by_fitness(population)[-1]
    max_of_generation.append(fitness_functions.target(max_individual_of_generation))
    if i >= generations:
        break

    i += 1

    population = population_pool.make_next_generation(population, mode=max)

i = 1
while True:
    min_individual_of_generation = population_pool.sort_population_by_fitness(population)[0]
    min_of_generation.append(fitness_functions.target(min_individual_of_generation))
    if i >= generations:
        break

    i += 1

    population = population_pool.make_next_generation(population, mode=min)

xpoints = range(generations)

plt.plot(xpoints, max_of_generation)
plt.show()

plt.plot(xpoints, min_of_generation)
plt.show()

best_individual = population_pool.sort_population_by_fitness(population)[-1]
print("\n🔬 FINAL RESULT")
print(best_individual.dna, fitness_functions.target(best_individual))    