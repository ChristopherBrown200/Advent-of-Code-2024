with open('12.txt') as f:
    text = f.read()

def searchGarden(currRow: int, currCol: int, plant:str, garden: list[list[str]], plants: set):
    
    if currRow - 1 > -1 and (currRow-1, currCol) not in plants and garden[currRow-1][currCol] == plant:
        plants.add((currRow-1, currCol))
        searchGarden(currRow-1, currCol, plant, garden, plants)

    if currRow + 1 < len(garden) and (currRow+1, currCol) not in plants and garden[currRow+1][currCol] == plant:
        plants.add((currRow+1, currCol))
        searchGarden(currRow+1, currCol, plant, garden, plants)

    if currCol - 1 > -1 and (currRow, currCol-1) not in plants and garden[currRow][currCol-1] == plant:
        plants.add((currRow, currCol-1))
        searchGarden(currRow, currCol-1, plant, garden, plants)

    if currCol + 1 < len(garden[0]) and (currRow, currCol+1) not in plants and garden[currRow][currCol+1] == plant:
        plants.add((currRow, currCol+1))
        searchGarden(currRow, currCol+1, plant, garden, plants)

def getFences(plants: set) -> int:
    fences = 0
    for plant in plants:
        r = plant[0]
        c = plant[1]
        if (r-1, c) not in plants:
            fences += 1
        if (r+1, c) not in plants:
            fences += 1
        if (r, c-1) not in plants:
            fences += 1
        if (r, c+1) not in plants:
            fences += 1

    return fences

def accountForDuplicates(sides: list[set]):
    wasDuplicate = True

    while(wasDuplicate):
        wasDuplicate = False
        for a in sides:
            for b in sides:
                if len(a.intersection(b)) > 0 and a != b:
                    wasDuplicate = True
                    break
            if wasDuplicate:
                break

        if wasDuplicate:
            sides.remove(a)
            sides.remove(b)
            sides.append(a.union(b))

def getSides(plants: set) -> int:
    topSides = []
    bottomSides = []
    leftSides = []
    rightSides = []
    for plant in plants:
        r = plant[0]
        c = plant[1]
        if (r-1, c) not in plants:
            wasSide = False
            for side in topSides:
                if (r-1, c-1) in side or (r-1, c+1) in side:
                    side.add((r-1, c))
                    wasSide = True
            if not wasSide:
                topSides.append({(r-1, c)})

        if (r+1, c) not in plants:
            wasSide = False
            for side in bottomSides:
                if (r+1, c-1) in side or (r+1, c+1) in side:
                    side.add((r+1, c))
                    wasSide = True
            if not wasSide:
                bottomSides.append({(r+1, c)})

        if (r, c+1) not in plants:
            wasSide = False
            for side in rightSides:
                if (r-1, c+1) in side or (r+1, c+1) in side:
                    side.add((r, c+1))
                    wasSide = True
            if not wasSide:
                rightSides.append({(r, c+1)})
        
        if (r, c-1) not in plants:
            wasSide = False
            for side in leftSides:
                if (r-1, c-1) in side or (r+1, c-1) in side:
                    side.add((r, c-1))
                    wasSide = True
            if not wasSide:
                leftSides.append({(r, c-1)})

    accountForDuplicates(topSides)
    accountForDuplicates(bottomSides)
    accountForDuplicates(rightSides)
    accountForDuplicates(leftSides)
    
    return len(topSides) + len(bottomSides) + len(leftSides) + len(rightSides)

garden = []
rows = text.split('\n')
for row in rows:
    garden.append(list(row))

cost1 = 0
cost2 = 0

for r in range(len(garden)):
    for c in range(len(row)):
        plant = garden[r][c]
        if plant == '-':
            continue

        plants = {(r, c)}
        searchGarden(r, c, plant, garden, plants)
        for p in plants:
            garden[p[0]][p[1]] = '-'

        # Part 1
        cost1 += len(plants) * getFences(plants)

        # Part 2
        cost2 += len(plants) * getSides(plants)

print(cost1)
print(cost2)