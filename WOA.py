import numpy as np

class WhaleOptimization:
    def __init__(self, population_size, max_iter):
        self.population_size = population_size
        self.max_iter = max_iter

    def optimize(self, fitness_function, dim):
        positions = np.random.rand(self.population_size, dim)
        best_solution = min(positions, key=fitness_function)

        for _ in range(self.max_iter):
            for i in range(self.population_size):
                a = 2 - _ * (2 / self.max_iter)
                r = np.random.rand()
                A = 2 * a * r - a
                C = 2 * np.random.rand()

                if np.abs(A) < 1:
                    positions[i] = best_solution - A * np.abs(C * best_solution - positions[i])
                else:
                    rand_solution = positions[np.random.randint(self.population_size)]
                    positions[i] = rand_solution - A * np.abs(C * rand_solution - positions[i])

            best_solution = min(positions, key=fitness_function)
        return best_solution

fitness_function = lambda x: np.sum(x**2)  # Example function
woa = WhaleOptimization(population_size=20, max_iter=50)
best_solution = woa.optimize(fitness_function, dim=3)
