from board import Board
import random
import time

my_board = Board(5)

###------------------------------------------------------------------------###
## Generates the random populations to compare later on
# Status: Done
def population(size):

    population = []
    # generating number of random populations
    for _ in range(size):
        my_board = Board(5)
        chromosome = my_board.encode()
        population.append(chromosome)
    # returns string of numbers
    # goes by column and what row the queen is in
    return population

###------------------------------------------------------------------------###
## Shows how desirable each chromosome is (fitness score lol)
# Status: Done
def fitness_scores(random_populations):

    # since the algorithm we looked over in class perfers higher fitness scores, we need to invert the fitness scores
    max_fitness = (5*4)/2 # = 10

    inverted_scores = []
    # creates a temporary board for testing
    temporary_board = Board(5)
    # looks at each chromosome in the 8 randomized populations
    for chromosome in random_populations:
        # copies the chromosomes to the temporary board
        temporary_board.decode(chromosome)
        individual_fitness = temporary_board.get_fitness()
        # calculates the inverted scores, (10 being best, 0 being worst)
        inverted_scores.append(int(max_fitness - individual_fitness))

    return inverted_scores

def selection(inverted_scores, population):
    
    parents = []

    total_fitness = 0
    for i in inverted_scores:
        # adds all inverted scores together
        total_fitness += i

    # create each individual probability for each fitness score
    probabilities = []
    for score in inverted_scores:
        probabilities.append(score/total_fitness)

    cumulative_probability = []
    current = 0
    for i in probabilities:
        current += i
        cumulative_probability.append(current)

    for _ in range(len(population)):
        # generate the random number between 0 and 1
        r = round(random.random(), 2)
        for j, cumulative in enumerate(cumulative_probability):
            if r <= cumulative:
                parents.append(population[j])
                break

    return parents

def crossover(first_parent, second_parent):

    # selects a random point from the parent, cannot be first or last column
    crossover_point = random.randint(1, 4)

    next_generation_1 = first_parent[:crossover_point] + second_parent[crossover_point:]
    next_generation_2 = second_parent[:crossover_point] + first_parent[crossover_point:]

    return next_generation_1, next_generation_2

def mutation(chromosome):
    # generates a random position to mutate
    mutated_gene = random.randint(0, 4)
    # generates a random number to replace current number in random position
    random_value = str(random.randint(0, 4))

    chromosome_list = list(chromosome)
    chromosome_list[mutated_gene] = random_value
    return "".join(chromosome_list)


def main():

    total_generation = 100
    max_fitness = (5*4)/2

    starting_time = time.time()

    # ending_time = time.time()
    # creates 8 random states

    best_board = None
    best_fitness = -1

    random_populations = population(8)

    for generation in range(total_generation):

        fitness = fitness_scores(random_populations)

        for i, chromosome in enumerate(random_populations):
            if fitness[i] > best_fitness:
                best_fitness = fitness[i]
                best_board = chromosome

            if fitness[i] == max_fitness:
                ending_time = time.time()
                best_board = Board(5)
                best_board.decode(chromosome)

                print(f"Running time: {((ending_time - starting_time) * 1000):.2f}ms")
                best_board.print_map()
                return

        gene_pool = selection(fitness, random_populations)

        new_generation = []

        for i in range(0,7,2):
            first_parent = gene_pool[i]
            if i+1 < len(gene_pool):
                second_parent = gene_pool[i+1]
            else:
                second_parent = gene_pool[0]

            first_child, second_child = crossover(first_parent, second_parent)
            new_generation.append(mutation(first_child))
            new_generation.append(mutation(second_child))
            
        random_populations = new_generation

main()