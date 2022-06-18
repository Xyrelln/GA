import random
import matplotlib.pyplot as plt
import chromosome, fitness_functions, population_pool


boundaries = (0, 15)
generations = 100

population = population_pool.generate_population(size=100, x_boundaries=boundaries, y_boundaries=boundaries, z_boundaries=boundaries)

i = 1
best_of_generation = []
while True:
    best_individual_of_generation = population_pool.sort_population_by_fitness(population)[-1]
    best_of_generation.append(fitness_functions.target(best_individual_of_generation))
    if i >= generations:
        break

    i += 1

    population = population_pool.make_next_generation(population)

xpoints = range(100)
plt.plot(xpoints, best_of_generation)
plt.show()

best_individual = population_pool.sort_population_by_fitness(population)[-1]
print("\n🔬 FINAL RESULT")
print(best_individual, fitness_functions.target(best_individual))    