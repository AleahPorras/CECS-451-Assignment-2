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

def selection(scores):

    max_score = max(scores)

    normalized_scores = []
    for score in scores:
        normalized_scores.append(max_score - score + 1)

    total_score = sum(normalized_scores)
    probabilities = []
    for score in normalized_scores:
        probabilities.append(score/total_score)
    
    # generates a random float value
    r = random.random()

    current = 0

    for i in range(len(probabilities)):
        current = current + probabilities[i]
        if current >= r:
            return probabilities[i]

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
    fitness = fitness_scores(random_populations)
    print(fitness)
    print(selection(fitness))



main()