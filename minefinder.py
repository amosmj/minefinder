import random
import math

def buildGrid(width , height,difficulty):
    grid = []
    #xRow = [0] * width
    for y in range(height):
        grid.append([0] * width)    
    
    mines = math.floor((width*height/10))
    minePlace = []
    for m in range(mines):
        validMine = False
        while validMine == False:
            validMine = True
            newMineLoc = random.randint(0,width*height)
            for mp in range(len(minePlace)):
                if mp == newMineLoc:
                    validMine = False
        minePlace.append(newMineLoc)
    print("mine placed: " ,str(minePlace))
    for mp in minePlace:
        x = math.floor(mp/width)
        y = mp % width
        print('placment: ',str(mp),', X: ',str(x), ', Y: ',str(y))
        #print('placement row: ',grid[y])
        print('placement cell: ', grid[y][x])
        grid[y][x] = 9
        #for i in grid:
        #    print(i)
    return grid

print('Welcome to MineFinder')
width = int(input('how wide do you want the grid?'))
height = int(input('how high do you want the grid?'))
#difficulty = input('how tough do you want the grid?')
#may need to sanitize inputs
field = buildGrid(width, height, 0)
for y in field:
    print(y)
    