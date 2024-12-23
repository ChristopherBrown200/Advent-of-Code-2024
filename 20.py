import sys
sys.setrecursionlimit(10**6)

text = open('20.txt').read()

grid = []
dotCount = 0
for r, line in enumerate(text.split('\n')):
    row = []
    for c, space in enumerate(line):
        match space:
            case '#': row.append(False)
            case '.': 
                row.append(True)
                dotCount += 1
            case 'S':
                rStart, cStart = (r, c)
                row.append(True)
            case 'E':
                End = (r, c)
                row.append(True)
    grid.append(row)

width = len(row)-1
height = len(grid)-1

ogPath = []
ScoreNoCheat = 10 ** 6

def findBestPath(rCurr: int, cCurr: int, visted: list = [], score: int = 0) -> int:
    visted.append((rCurr, cCurr))

    global ogPath
    ogPath = visted.copy()


    if (rCurr, cCurr) == End:
        global ScoreNoCheat
        ScoreNoCheat = score
        ogPath = visted.copy()
        return

    if rCurr-1 > 0 and (rCurr-1, cCurr) not in visted and grid[rCurr-1][cCurr]:
        findBestPath(rCurr-1, cCurr, visted.copy(), score + 1)

    elif rCurr+1 < height and (rCurr+1, cCurr) not in visted and grid[rCurr+1][cCurr]:
        findBestPath(rCurr+1, cCurr, visted.copy(), score + 1)

    elif cCurr-1 > 0 and (rCurr, cCurr-1) not in visted and grid[rCurr][cCurr-1]:
        findBestPath(rCurr, cCurr-1, visted.copy(), score + 1)

    elif cCurr+1 < width and (rCurr, cCurr+1) not in visted and grid[rCurr][cCurr+1]:
        findBestPath(rCurr, cCurr+1, visted.copy(), score + 1)


findBestPath(rStart, cStart)

def printPath(path, point):
    count = 0
    for r, row in enumerate(grid):
        printRow = ''
        for c, space in enumerate(row):
            if (r,c) == point:
                printRow += '*'
            elif (r,c) in path:
                printRow += 'O'
            elif not space:
                printRow += "|"
            else:
                printRow += '.'
                count += 1
        print(printRow)
    print(count-1, '.')
    input()


# Part 1
saves = []
for r, row in enumerate(grid):
    for c, space in enumerate(row):
        if not grid[r][c]:
            possCheats = -1

            # horizontal Cheat
            if (r, c-1) in ogPath and (r, c+1) in ogPath:
                firstIndex = ogPath.index((r, c-1))+1
                secondIndex = ogPath.index((r, c+1))
                if firstIndex > secondIndex:
                    temp = firstIndex
                    firstIndex = secondIndex+1
                    secondIndex = temp-1
                
                newPath = ogPath[:firstIndex] + ogPath[secondIndex:]
                possCheats = ScoreNoCheat - len(newPath)


            # vertical Cheat
            if (r-1, c) in ogPath and (r+1, c) in ogPath:
                firstIndex = ogPath.index((r-1, c))+1
                secondIndex = ogPath.index((r+1, c))
                if firstIndex > secondIndex:
                    temp = firstIndex
                    firstIndex = secondIndex+1
                    secondIndex = temp-1

                newPath = ogPath[:firstIndex] + ogPath[secondIndex:]
                possCheats = ScoreNoCheat - len(newPath)

            if possCheats >= 100:
                saves.append(saves)

print(len(saves))

# Part 2

def getSkipTime(pointA: tuple[int, int], pointB: tuple[int, int]) -> int:
    dis = abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])
    return dis

saves = []

for a, pointA in enumerate(ogPath):
    for pointB in ogPath[a+2:]:
        if getSkipTime(pointA, pointB) > 20:
            continue

        firstIndex = ogPath.index(pointA)+1
        secondIndex = ogPath.index(pointB)

        newPath = ogPath[:firstIndex] + ogPath[secondIndex:]
        newTime = len(newPath) + getSkipTime(pointA, pointB)
        timeSaved = ScoreNoCheat - newTime + 2
        if timeSaved >= 100:
            saves.append(timeSaved)

print(len(saves))
