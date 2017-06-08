import numpy
numpy.set_printoptions(threshold = 10000)

def buildGrid(width , height, difficulty):
    #slack study.py user mikelane basically wrote this for me
    #He collapsed 20 or so lines of code into 1
    difficulty_dictionary = {'1' : [0.9 ,0.1 ],'2' : [0.75,0.25],'3' : [0.6 ,0.4 ]}
    #this like creates the playing field, populated with 0 (nothing) or 9 (a mine)
    #the difficulty parameter sets the probablity based on the dictionary above
    grid = numpy.random.choice(a=[0,9],size=(height, width),p=difficulty_dictionary[difficulty])
    #padding the array to make searching it easier
    grid = numpy.lib.pad(array = grid, pad_width=(1,1), mode = 'constant', constant_values = (0))
    print(grid)
    
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
                    print(testSquare)
                    #next count the 9s in the window
                    #now write that number to the cell
            
    print(grid)
    return grid

def testCell(column, row):
    return findings

def solvePuzzle(grid):
    return 0

print('Welcome to MineFinder')
width = int(input('how wide do you want the grid?'))
height = int(input('how high do you want the grid?'))
difficulty = input('Enter 1, 2, or 3 for easy, medium, or hard:')
#may need to sanitize inputs
field = buildGrid(width, height, difficulty)    