with open('6.txt') as f:
    text = f.read()

vistedPoints = []
vistedPoints2 = []

# Part 1
text = text.replace('^', 'x')
map = text.split('\n')

for l, line in enumerate(map):
    if 'x' in line:
        currLoc = [l, line.find('x')]

moveVector = [-1 ,0]
nextLoc = [currLoc[0] + moveVector[0], currLoc[1] + moveVector[1]]

while nextLoc[0] > -1 and nextLoc[1] > -1 and nextLoc[0] < len(map) and nextLoc[1] < len(map[0]):
    if map[nextLoc[0]][nextLoc[1]] == '#':
        moveVector = [moveVector[1], -moveVector[0]]
    else:
        map[nextLoc[0]] = map[nextLoc[0]][:nextLoc[1]] + 'x' + map[nextLoc[0]][nextLoc[1]+1:]
        if currLoc not in vistedPoints:
            vistedPoints.append(currLoc.copy())
        currLoc = nextLoc.copy()
    nextLoc = [currLoc[0] + moveVector[0], currLoc[1] + moveVector[1]]

vistedPoints.append(currLoc)

total = 0
for line in map:
    total += line.count('x')

print(total)

# Part 2
with open('6.txt') as f:
    text = f.read()

map = text.split('\n')

for l, line in enumerate(map):
        if '^' in line:
            startLoc = [l, line.find('^')]
vistedPoints = vistedPoints[1:]

total = 0

for i, p in enumerate(vistedPoints):
    newMap = map.copy()

    newMap[p[0]] = newMap[p[0]][:p[1]] + '#' + newMap[p[0]][p[1]+1:]

    currLoc = startLoc.copy()
    moveVector = [-1 ,0]
    nextLoc = [currLoc[0] + moveVector[0], currLoc[1] + moveVector[1]]
    pastLoc = []

    while nextLoc[0] > -1 and nextLoc[1] > -1 and nextLoc[0] < len(newMap) and nextLoc[1] < len(newMap[0]):
        if [currLoc, moveVector] in pastLoc:
            total += 1            
            break

        if newMap[nextLoc[0]][nextLoc[1]] == '#':
            moveVector = [moveVector[1], -moveVector[0]]
        else:
            newMap[nextLoc[0]] = newMap[nextLoc[0]][:nextLoc[1]] + 'x' + newMap[nextLoc[0]][nextLoc[1]+1:]
            pastLoc.append([currLoc.copy(), moveVector.copy()])
            currLoc = nextLoc.copy()

        nextLoc = [currLoc[0] + moveVector[0], currLoc[1] + moveVector[1]]
        
print(total)