import sys
sys.setrecursionlimit(10**6)

def printFloor():
    global floor
    for row in floor:
        printout = ''
        for space in row:
            if space:
                printout += '.'
            else:
                printout += '#'
        print(printout)

stepsAtPoints = dict()
bestPath = set()
def search(finalpoint: int = 70, row: int = 0, col: int = 0, prevVisted: set = set()) -> bool:
    if (row, col) == (finalpoint, finalpoint):
        global bestPath
        if len(prevVisted) < len(bestPath) or len(bestPath) == 0:
            bestPath = prevVisted.copy()
        return True

    global floor
    visted = prevVisted.copy()
    visted.add((row, col))

    if (row, col) in stepsAtPoints:
        if len(visted) < stepsAtPoints[(row, col)]:
            stepsAtPoints[(row, col)] = len(visted)
        else:
            return
    else:
        stepsAtPoints[(row, col)] = len(visted)

    possible = False
    if row-1 >= 0 and (row-1, col) not in visted and floor[row-1][col]:
        if search(finalpoint, row-1, col, visted):
            possible = True

    if row+1 <= finalpoint and (row+1, col) not in visted and floor[row+1][col]:
        if search(finalpoint, row+1, col, visted):
            possible = True

    if col-1 >= 0 and (row, col-1) not in visted and floor[row][col-1]:
        if search(finalpoint, row, col-1, visted):
            possible = True

    if col+1 <= finalpoint and  (row, col+1) not in visted and floor[row][col+1]:
        if search(finalpoint, row, col+1, visted):
            possible = True
    
    return possible

with open('18.txt') as f:
    text = f.read()

bytes = text.split('\n')

fallingBytes = []

for byte in bytes:
    col, row = map(int, byte.split(','))
    fallingBytes.append((row, col))

floor = []
row = [True] * 71
for _ in range(71):
    floor.append(row.copy())

nBytes = 1024
for i in range(nBytes):
    row, col = fallingBytes[i]
    floor[row][col] = False

# printFloor()

# Part 1
search()
print(len(bestPath))

# Part 2
for i in range(nBytes, len(fallingBytes)):
    row, col = fallingBytes[i]
    floor[row][col] = False
    if fallingBytes[i] in bestPath:
        stepsAtPoints = dict()
        bestPath = set()
        if not search():
            print(f'{col},{row}')
            exit()