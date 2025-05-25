import numpy as np
import pickle
import matplotlib.pyplot as plt
from ortools.sat.python import cp_model

#generate all possible orientations of the pieces
def flip_and_rotate(piece):
    orientations = []
    for i in range(4):
        rotated = np.rot90(piece, i)
        for j in range(2):
            if not any(rotated.shape == existing.shape and np.array_equal(rotated,existing) for existing in orientations):
                orientations.append(rotated)
            rotated = np.fliplr(rotated)
    return orientations

# load pieces from a file. they can be rotated and flipped
with open('C:/Users/abrah/OneDrive/Desktop/code/miscellaneous python/iq game code/enigma/enigma_pieces.pkl', 'rb') as file:
    pieces = pickle.load(file)

#specify whether you want to see all possible solutions or just one
allSols = True
#See the solutions, or just find out how many there are? (only relevant if allSols = True)
displaySols = 1

#specify starting piece number (shape), row, and column
starting_pieces = [
    [(flip_and_rotate(pieces[3])[7],1,0)],
    [(flip_and_rotate(pieces[6])[3],3,1)],
    [(flip_and_rotate(pieces[7])[3],3,4)],
    #[(flip_and_rotate(pieces[8])[5],2,2)],
    #[(flip_and_rotate(pieces[9])[1],3,2)],
    [(flip_and_rotate(pieces[10])[1],2,3)],
]
'''
piece 0 = pink, piece 1 = red
piece 2 = orange, piece 3 = yellow.
piece 4 = green. piece 5 = aquamarine.
piece 6 = teal, piece 7 = cyan, 
piece 8 = big blue, piece 9 = small blue.
piece 10 = brown 
'''

#define board shape
board_rows = 5
board_cols = 10
 # "humanity", "missile", 
keyword = 'metallic'

lettergrid = [
#    ['a', ' ', 'b', ' ', 'c', ' ', 'd', ' ', 'e', ' '],
#    [' ', 'f', ' ', 'g', ' ', 'h', ' ', 'i', ' ', 'j'],
#    ['k', ' ', 'l', ' ', 'm', ' ', 'n', ' ', 'o', ' '],
#    [' ', 'p', ' ', 'r', ' ', 's', ' ', 't', ' ', 'u'],
#    ['v', ' ', 'w', ' ', 'x', ' ', 'y', ' ', 'z', ' ']

    [' ', 'i', ' ', ' ', 'a', ' ', 'y', 'b', ' ', 'o'],
    ['s', ' ', 'c', 'o', ' ', 'm', 'e', ' ', 'h', ' '],
    ['g', ' ', 't', ' ', 'u', ' ', 'l', ' ', 'n', 'i'],
    [' ', 'a', 'n', ' ', ' ', 'p', ' ', 'r', ' ', 'e'],
    ['l', ' ', ' ', 'e', 'd', ' ', 't', 's', ' ', ' ']
]

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#when all solutions are wanted, this class handles callback
class AllSolutions(cp_model.CpSolverSolutionCallback):
    def __init__(self, placements, vars):
        super().__init__()
        self.vars = vars
        self.placements = placements
        self.num_sols = 0

    def on_solution_callback(self):
        self.num_sols += 1
        if displaySols == True: 
            create_sol_grid(self.placements, self.vars, self)
    '''
        self.current_sol = create_sol_grid(self.placements, self.vars, self)
        if not np.array_equal(self.last_sol, self.current_sol):
            self.num_sols += 1
            if displaySols:
                plot_grid(self.current_sol)
        self.last_sol = self.current_sol
    '''
    def get_num_sols(self):
        return self.num_sols

#given the array representing a piece, find what number piece it is
def piecenum(piece):
    for piece_num, original_piece in enumerate(pieces):
        if any(np.array_equal(piece,orientation) for orientation in flip_and_rotate(original_piece)):
            return piece_num+1

#generate all possible placements as a list of [orientation, x, y]
#note that a "placement" on the board does specify an orientation
#also, this function assumes no superfluous rows or columns in a piece array, as well as a rectangular board
def possible_placements(piece):
    placements = []
    for orientation in flip_and_rotate(piece):
        for row in range(board_rows-orientation.shape[0]+1):
            for col in range(board_cols-orientation.shape[1]+1):
                placements.append((orientation, row, col))
    return placements

#Function that loops through all boolean variables, returning a dictionary linking each grid spot with the variables
# that, if true, would result in that spot being covered. 
def grid_coverage(placements_list, vars_list):
    coverage = {}
    for row in range(board_rows):
        for col in range(board_cols):
            coverage[row,col] = []
    for piece_num, piece_list in enumerate(placements_list):
        for placement_num, (piece, placement_row, placement_col) in enumerate(piece_list):
            for piece_row in range(piece.shape[0]):
                for piece_col in range(piece.shape[1]):
                    if piece[piece_row,piece_col]:
                        coverage[(placement_row+piece_row,placement_col+piece_col)].append(vars_list[piece_num][placement_num])
    return coverage
    
#Function takes in a keyword and returns a dict of tuples describing how many times each letter appears in the keyword
def letter_frequency(keyword):
    freq = {}
    word_letters = list(keyword.lower())
    for letter in alphabet:
        times_in_word = word_letters.count(letter)
        freq[letter] = times_in_word
    return freq

#Function that loops through all boolean variables, returning a dictionary linking each letter on the grid 
# with the variables that, if true, would result in that spot being covered. If a single variable uncovers a letter 
#multiple times, it will appear multiple times in the list.
def letter_coverage(placements_list, vars_list):
    letters = {}
    for row in range(board_rows):
        for col in range(board_cols):
            l = lettergrid[row][col]
            if l != ' ':
                letters[l] = []
    for piece_num, piece_list in enumerate(placements_list):
        for placement_num, (piece, placement_row, placement_col) in enumerate(piece_list):
            for piece_row in range(piece.shape[0]):
                for piece_col in range(piece.shape[1]):
                    if piece[piece_row,piece_col]==1.02 and lettergrid[placement_row+piece_row][placement_col+piece_col] != ' ':
                        letters[lettergrid[placement_row+piece_row][placement_col+piece_col]].append(vars_list[piece_num][placement_num])
    return letters

#given the solution variables and placements, construct an array to represent the solution.
def create_sol_grid(placements_list, vars_list, solver):
    solution_grid = np.zeros((board_rows, board_cols))
    for i, piece_placements in enumerate(placements_list):
        for j, (piece, row, col) in enumerate(piece_placements):
            piece_num = piecenum(piece)
            if solver.Value(vars_list[i][j]):
                solution_grid[row:row+piece.shape[0], col:col+piece.shape[1]] += piece_num * piece
    #print("Solution grid:")
    #print(solution_grid)
    plot_grid(solution_grid)

def plot_grid(solution_grid):
    size = 1400
    colors = np.array(["white","xkcd:pink","red","orange","yellow","xkcd:green","aquamarine","xkcd:teal","cyan","blue","darkblue","brown"])
    for row in range(solution_grid.shape[0]):
            for col in range(solution_grid.shape[1]):
                plt.scatter(col, -row, s = size, c=colors[int(solution_grid[row,col])])
                z=0
                if colors[int(solution_grid[row,col])] == "white":
                    z=4
                plt.text(col, -row, lettergrid[row][col], fontsize=14, horizontalalignment='center', verticalalignment='center', zorder = z)
                if solution_grid[row,col]%1 > 0.01:
                    plt.scatter(col, -row, s = size*0.5, c='white')
                    plt.text(col, -row, lettergrid[row][col], fontsize=14, horizontalalignment='center', verticalalignment='center')
    plt.xlim(-0.5, solution_grid.shape[1]-0.5)
    plt.ylim(-solution_grid.shape[0]-0.5,0.5)
    plt.gca().set_aspect(1, adjustable='datalim')
    plt.title('keyword: '+keyword, fontsize = 20)
    plt.tight_layout()
    plt.gca().tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    plt.show()


        
#first, ensure the grid makes sense for the keyword
keyword_freq = letter_frequency(keyword)
grid_freq = letter_frequency(''.join([l for row in lettergrid for l in row if l != ' ']))
for letter in keyword_freq:
    if keyword_freq[letter] > grid_freq[letter]:
        raise ValueError("letters in grid can't satisfy keyword!")
        
#plot starting piece configuration
starting_grid = np.zeros((board_rows, board_cols))
for [(starting_piece,row,col)] in starting_pieces:
    piece_num = piecenum(starting_piece)
    starting_grid[row:row+starting_piece.shape[0], col:col+starting_piece.shape[1]] += piece_num * starting_piece
plot_grid(starting_grid)

#generate a list of sub-lists, each list corresponds to a different piece. 
#Each sub-list contains all possible placements for the piece.
placements_list = []
for piece in pieces:
    if not any(
    any(np.array_equal(piece, orient) for orient in flip_and_rotate(starting_piece[0][0]))
    for starting_piece in starting_pieces):
        placements_list.append(possible_placements(piece))
#there's only one possible placement for starting pieces.
for piece_placement in starting_pieces:
    placements_list.append(piece_placement)

Model = cp_model.CpModel()

#create boolean variables: if a certain piece is at a certain placement, it's true. Otherwise, it's false.
#Each boolean variable in the list corresponds directly to the piece and placement at the variable's location in the placement list. 
vars_list = []
for i, piece_list in enumerate(placements_list):
    piece_vars = []
    for j in range(len(piece_list)):
        var = Model.NewBoolVar(f'piece_{i}_placement_{j}')
        piece_vars.append(var)
    vars_list.append(piece_vars)

#constraints:

#exactly one boolean variable can (and must) be true for each piece. Therefore, the sum of all boolean variables for each piece must be 1.
for piece_vars in vars_list:
    Model.add(sum(piece_vars)==1)

#using the grid coverage, enforce that the sum of all boolean variables for each grid location must be 1
coverage = grid_coverage(placements_list, vars_list)
for location in coverage:
    Model.add(sum(coverage[location])==1)

#the revealed letters must make up the keyword!
freq = letter_frequency(keyword)
letters = letter_coverage(placements_list, vars_list)
for letter in letters:
    Model.add(sum(letters[letter])==freq[letter])

# Solve the model
solver = cp_model.CpSolver()
solution = solver.Solve(Model)

#if there's a solution, plot it.
if solution in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    if allSols:
        solution_printer = AllSolutions(placements_list,vars_list)
        solver.SearchForAllSolutions(Model, solution_printer)
        print("Total number of solutions:")
        print(solution_printer.get_num_sols())
    else:
        create_sol_grid(placements_list, vars_list, solver)
else:
    print("No solution found.")