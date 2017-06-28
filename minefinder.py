import numpy
numpy.set_printoptions(threshold = 10000)

def buildGrid(width , height, difficulty):
    #slack study.py user mikelane basically wrote this for me
    #He collapsed 20 or so lines of code into 1
    difficulty_dictionary = {'1' : [0.9 ,0.1 ],'2' : [0.75,0.25],'3' : [0.6 ,0.4 ]}
    #this creates the playing field, populated with 0 (nothing) or 9 (a mine)
    #the difficulty parameter sets the probablity based on the dictionary above
    grid = numpy.random.choice(a=[0,9],size=(height, width),p=difficulty_dictionary[difficulty])
    #padding the array to make searching it easier
    grid = numpy.lib.pad(array = grid, pad_width=(1,1), mode = 'constant', constant_values = (0))
    #print(grid)
    
    #now I want to populate the number of mines adjacent to any cell
    for h in range(grid.shape[1]):
        for w in range(grid.shape[0]):
            #Is this a mine? If yes, move on, if no, test further
            if 9 != grid[h][w]:
                #Since it's not a mine, we need to figure out how many are
                #adjacent. I've padded the outer rows so I can do this with
                #3x3 looks. To avoid trying to look outside the array
                #I start in one row and one column and end in one row
                #and one column
                if h > 0 and h <= height and w > 0 and w <= width:
                    testSquare = grid[(h-1):(h+2),(w-1):(w+2)]
                    #print(testSquare)
                    #next count the 9s in the window
                    #now write that number to the cell
                    #print (testSquare)
                    squareVal = list(testSquare.flatten()).count(9)
                    testSquare[1:2,1:2] = squareVal
                    grid[(h-1):(h+2),(w-1):(w+2)] = testSquare

    #finally, strip the junk columns off of the top and bottom and both sides
    grid = numpy.delete(arr = grid, obj = [w], axis = 1)
    grid = numpy.delete(arr = grid, obj = [0], axis = 1)
    grid = numpy.delete(arr = grid, obj = [h], axis = 0)
    grid = numpy.delete(arr = grid, obj = [0], axis = 0)
    #output the grid
    return grid



def updateCell(testGrid, column, row, value):
    return testedGrid

def solvePuzzle(grid):
    
    return 0

if __name__ == "__main__":
    answerField = [[0]]
    testField = [[0]]
    print('Welcome to MineFinder')
    width = int(input('how wide do you want the grid?'))
    height = int(input('how high do you want the grid?'))
    difficulty = input('Enter 1, 2, or 3 for easy, medium, or hard:')
    #may need to sanitize inputs
    answerField = buildGrid(width, height, difficulty)  
    testField = numpy.zeros_like(answerField)
    #need to find an empty space to open to get started
    
    game_over = False
    guesses = 0
    
    while game_over == False:
        print(testField)
        print('Press Q to exit the program at any time')
        column = input('Which column contains the cell?')
        row = input('Which row contains the cell?')
        if column != 'Q' and column != 'q' and row != 'Q' and row !='q': 
            result = answerField[int(column), int(row)]
            if result == 9:
                #player found a bomb
                game_over = True
                print('BOOM! you lose')
            else:
                #no bomb found, update the grid and move on
                a = 1
        else:
            game_over = True
