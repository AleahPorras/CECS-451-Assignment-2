from board import Board
import random
import time

my_board = Board(5)

###------------------------------------------------------------------------###
## Generates the random populations to compare later on
# Status: Done
def population(size):

    population = []
    for _ in range(size):
        my_board = Board(5)
        chromosome = my_board.encode()
        population.append(chromosome)
    # return my_board.get_map()
    return population
    pass

def fitness_scores(random_populations):
    score = []
    temp = Board(5)
    for i in random_populations:
        temp.decode(i)
        fitness = temp.get_fitness()
        score.append(fitness)

    return score

def selection():
    pass

def crossover():
    pass

def mutation():
    pass


def main():
    # starting_timer = time.time()

    # ending_timer = time.time()

    # total_time = (ending_timer - starting_timer)*1000
    # print(f"Running time: {total_time}ms")
    my_board.print_map()

    random_populations = population(5)
    print(random_populations)
    print(fitness_scores(random_populations))

main()