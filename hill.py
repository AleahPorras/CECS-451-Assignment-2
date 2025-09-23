# import random
# import time
# from board import Board


# def hill_climb_algorithm(n):

#     starting_time = time.time()

#     # creation of the first board
#     initial_board = Board(n)

#     while True:

#         # print("Initial Board:")
#         # initial_board.print_map()

#         # calculates how many queens are attacking each other
#         fitness_score = initial_board.get_fitness()
#         # print(f"Current fitness: {fitness_score}")

#         if fitness_score == 0:
#             # print("Yay! Solution found.")
#             ending_time = time.time()
#             total_time = (ending_time - starting_time)*1000
#             print(f"Running time: {total_time:.2f}ms")
#             initial_board.print_map()
#             return 

#         # contains the best fitness score
#         current_best = fitness_score
#         best_board = None

#         for col in range(5):
#             for row in range(5):
#                 # checks if queen is not in the same spot
#                 if row != int(initial_board.encode()[col]):
#                     # create temporary board for testing
#                     temporary_board = Board(n)
#                     # copies the first board into the temporary
#                     temporary_board.decode(initial_board.encode())

#                     sucessor_list = list(temporary_board.encode())
#                     sucessor_list[col] = str(row)
#                     sucessor = "".join(sucessor_list)

#                     temporary_board.decode(sucessor)

#                     # find the fitness of the new board
#                     sucessor_fitness = temporary_board.get_fitness()

#                     # checks if the possible sucessor fitness score is better than the current fitness score
#                     if sucessor_fitness < fitness_score:
#                         current_best = sucessor_fitness
#                         best_board = temporary_board
#                     else:
#                         continue
            
#         # Updates the initial board if a better one is found
#         if best_board is not None and current_best < fitness_score:
#             initial_board = best_board    
#         else:
#             initial_board = Board(n)
#             fitness_score = initial_board.get_fitness()

#             best_board = initial_board
#             current_best = fitness_score

# def main():

#     hill_climb_algorithm(5)

# main()


import board
import time


#_________________________________________________finding the location of the queen_________________________________________________
def where_is_queen(row):
    #loop that goes through each of the rows and returns the number of the row the queen in on
    for i in range(5):
        if row[i] == 1:
            return i

#_________________________________________________main loop_________________________________________________
def main():

    #time stamp for later
    begin = time.time()
    #starting board
    current_board = board.Board(5)
    #starting fitness
    current_fitness = current_board.get_fitness()

    #loop only breaks when the 0 condition is met (found the best fitness)
    while current_fitness != 0:
        #setting the current benchmark
        better_board = current_board
        lowest_fitness = current_fitness
        #loops through each row
        for row in range(5):
            #checks for the queen location
            queen_location = where_is_queen(current_board.get_map()[row])
            #loops through each column
            for col in range(5):
                #creating a duplicate board so that we don't alter the actual one just yet
                ##string value of the current board
                encoding = current_board.encode()

                #copying onto new board object
                possible_board = board.Board(5)
                possible_board.decode(encoding)

                #skipping over the queen to avoid  breaking
                ##due to not wanting to have two queens on a row
                if col == queen_location:
                    continue
                #shifting the queen to another location by swapping
                possible_board.flip(row,queen_location)
                possible_board.flip(row, col)
                #gettng the fitness of the possible better location
                possible_fitness = possible_board.get_fitness()

                #if the possible fitness is better, we will update the board and the fitness we need to beat next
                if (possible_fitness < lowest_fitness):
                    better_board = possible_board
                    lowest_fitness = possible_fitness

                # better wasn;t found so we loop through the next row
                else:
                    continue
        #if the loop ends and we found a fitness lower than the start
        #that becomes the better state and fitness
        if lowest_fitness  < current_fitness :
            current_board = better_board
            current_fitness = lowest_fitness

        #if no better state is found we need to create a totally new board and start over
        else:
            current_board = board.Board(5)
            current_fitness = current_board.get_fitness()

            better_board = current_board
            lowest_fitness = current_fitness

    end_time = time.time()
    #printing of runtime
    print(f"{( end_time-begin)*1000:.2f} ms")
    #printing of the best baord
    current_board.print_map()


main()

