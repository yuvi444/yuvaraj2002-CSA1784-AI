import mlrose
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,max_attempts = 100, random_state = 2)
print('The best state found is: ', best_state)
print('The fitness at the best state is: ', best_fitness)
