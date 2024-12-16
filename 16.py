import sys
sys.setrecursionlimit(10**6)

scoresAtPoints = dict()
bestScore = 1000000000
onBestPath = set()

def searchMaze(maze: list[list[str]], currRow:int, currCol: int, dir: int = 0, currScore:int = 0, visted: set = set()):
    visted.add((currRow, currCol))
    
    if maze[currRow][currCol] == 'E':
        global bestScore
        global onBestPath
        if currScore < bestScore:
            bestScore = currScore
            onBestPath = visted.copy()
        elif currScore == bestScore:
            onBestPath = onBestPath.union(visted.copy())
        return

    if (currRow, currCol) in scoresAtPoints and scoresAtPoints[(currRow, currCol)] < currScore-1000:
        return
    else: 
        scoresAtPoints[(currRow, currCol)] = currScore

    # right
    if maze[currRow][currCol+1] != '#' and (currRow, currCol+1) not in visted:
        score = currScore + 1
        if dir in [1, 3]:
            score += 1000
        
        searchMaze(maze, currRow, currCol+1, 0, score, visted.copy())

    # Down
    if maze[currRow+1][currCol] != '#' and (currRow+1, currCol) not in visted:
        score = currScore + 1
        if dir in [0, 2]:
            score += 1000
        
        searchMaze(maze, currRow+1, currCol, 1, score, visted.copy())

    # Left
    if maze[currRow][currCol-1] != '#' and (currRow, currCol-1) not in visted:
        score = currScore + 1
        if dir in [1, 3]:
            score += 1000

        searchMaze(maze, currRow, currCol-1, 2, score, visted.copy())
    
    # Up
    if maze[currRow-1][currCol] != '#' and (currRow-1, currCol) not in visted:
        score = currScore + 1
        if dir in [0, 2]:
            score += 1000

        searchMaze(maze, currRow-1, currCol, 3, score, visted.copy())

with open('16.txt') as f:
    text = f.read()

rows = text.split('\n')
maze = [list(row) for row in text.split()]

score = searchMaze(maze, len(maze)-2, 1)
print(bestScore)
print(len(onBestPath))
