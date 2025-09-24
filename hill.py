import random
import time
from board import Board


def hill_climb_algorithm(n):

    starting_time = time.time()

    # creation of the first board
    initial_board = Board(n)

    while True:

        # print("Initial Board:")
        # initial_board.print_map()

        # calculates how many queens are attacking each other
        fitness_score = initial_board.get_fitness()
        # print(f"Current fitness: {fitness_score}")

        if fitness_score == 0:
            # print("Yay! Solution found.")
            ending_time = time.time()
            total_time = (ending_time - starting_time)*1000
            print(f"Running time: {total_time:.2f}ms")
            initial_board.print_map()
            return 

        # contains the best fitness score
        current_best = fitness_score
        best_board = None

        for col in range(5):
            for row in range(5):
                # checks if queen is not in the same spot
                if row != int(initial_board.encode()[col]):
                    # create temporary board for testing
                    temporary_board = Board(n)
                    # copies the first board into the temporary
                    temporary_board.decode(initial_board.encode())

                    sucessor_list = list(temporary_board.encode())
                    sucessor_list[col] = str(row)
                    sucessor = "".join(sucessor_list)

                    temporary_board.decode(sucessor)

                    # find the fitness of the new board
                    sucessor_fitness = temporary_board.get_fitness()

                    # checks if the possible sucessor fitness score is better than the current fitness score
                    if sucessor_fitness < fitness_score:
                        current_best = sucessor_fitness
                        best_board = temporary_board
                    else:
                        continue
            
        # Updates the initial board if a better one is found
        if best_board is not None and current_best < fitness_score:
            initial_board = best_board    
        # if a better board isnt found, randomly restart the board, then continue with hill search
        else:
            initial_board = Board(n)
            fitness_score = initial_board.get_fitness()

            best_board = initial_board
            current_best = fitness_score

def main():

    hill_climb_algorithm(5)

main()


