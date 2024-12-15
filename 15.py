def move(warehouse: list[list[str]], botLocation: tuple[int, int], move: str) -> tuple[int,int]:
    canMove = True
    match move:
        case '^':
            direction = (-1,0)
        case 'v':
            direction = (1,0)
        case '<':
            direction = (0,-1)
        case '>':
            direction = (0,1)
    
    desiredRow = botLocation[0] + direction[0]
    desiredcol = botLocation[1] + direction[1]

    checkRow = desiredRow
    checkCol = desiredcol

    while warehouse[checkRow][checkCol] != '.':
        if warehouse[checkRow][checkCol] == '#':
            canMove = False
            break

        checkRow += direction[0]
        checkCol += direction[1]

    if canMove:
        if warehouse[desiredRow][desiredcol] == 'O':
            warehouse[checkRow][checkCol] = 'O'
            warehouse[desiredRow][desiredcol] = '.'
        return (desiredRow, desiredcol)
    return botLocation

def moveBoxLeft(warehouse:list[list[str]], row: int, col: int) -> bool:
    if warehouse[row][col-1] == '.':
        warehouse[row][col-1] = '['
        warehouse[row][col] = ']'
        warehouse[row][col+1] = '.'
        return True
    
    if warehouse[row][col-1] == '#':
        return False
    
    if moveBoxLeft(warehouse, row, col-2):
        warehouse[row][col-1] = '['
        warehouse[row][col] = ']'
        warehouse[row][col+1] = '.'
        return True

def moveBoxRight(warehouse: list[list[str]], row: int, col: int ) -> bool:
    if warehouse[row][col+2] == '.':
        warehouse[row][col] = '.'
        warehouse[row][col+1] = '['
        warehouse[row][col+2] = ']'
        return True

    if warehouse[row][col+2] == '#':
        return False
    
    if moveBoxRight(warehouse, row, col+2):
        warehouse[row][col] = '.'
        warehouse[row][col+1] = '['
        warehouse[row][col+2] = ']'
        return True

def moveBoxVertical(warehouse: list[list[str]], row: int, col: int, dr: int, copy: bool = True) -> bool:
    if warehouse[row+dr][col] == '.' and warehouse[row+dr][col+1] == '.':
        warehouse[row+dr][col] = '['
        warehouse[row+dr][col+1] = ']'
        warehouse[row][col] = '.'
        warehouse[row][col+1] = '.'
        return True
    
    if warehouse[row+dr][col] == '#' or warehouse[row+dr][col+1] == '#':
        return False
    
    if warehouse[row+dr][col] == '[':
        if moveBoxVertical(warehouse, row+dr, col, dr):
            warehouse[row+dr][col] = '['
            warehouse[row+dr][col+1] = ']'
            warehouse[row][col] = '.'
            warehouse[row][col+1] = '.'
            return True

    if warehouse[row+dr][col] == ']' and warehouse[row+dr][col+1] == '.':
        if moveBoxVertical(warehouse, row+dr, col-1, dr):
            warehouse[row+dr][col] = '['
            warehouse[row+dr][col+1] = ']'
            warehouse[row][col] = '.'
            warehouse[row][col+1] = '.'
            return True
        
    if warehouse[row+dr][col] == '.' and warehouse[row+dr][col+1] == '[':
        if moveBoxVertical(warehouse, row+dr, col+1, dr):
            warehouse[row+dr][col] = '['
            warehouse[row+dr][col+1] = ']'
            warehouse[row][col] = '.'
            warehouse[row][col+1] = '.'
            return True
        
    if warehouse[row+dr][col] == ']' and warehouse[row+dr][col+1] == '[':
        if copy:
            tempWarehouse = []
            for r in warehouse:
                tempWarehouse.append(r.copy())
            canMove = moveBoxVertical(tempWarehouse, row+dr, col-1, dr, False) and moveBoxVertical(tempWarehouse, row+dr, col+1, dr, False)
            if canMove:
                moveBoxVertical(warehouse, row+dr, col-1, dr, False)
                moveBoxVertical(warehouse, row+dr, col+1, dr, False)
                warehouse[row+dr][col] = '['
                warehouse[row+dr][col+1] = ']'
                warehouse[row][col] = '.'
                warehouse[row][col+1] = '.'
                return True
        else:
            if moveBoxVertical(warehouse, row+dr, col-1, dr, False) and moveBoxVertical(warehouse, row+dr, col+1, dr, False):
                warehouse[row+dr][col] = '['
                warehouse[row+dr][col+1] = ']'
                warehouse[row][col] = '.'
                warehouse[row][col+1] = '.'
                return True

    return False

def moveBot(warehouse: list[list[str]], botRow: int, botCol: int, move: str) -> tuple[int, int]:
    dr = 0
    dc = 0
    match move:
        case '<':
            dc = -1
        case '>':
            dc = 1

        case '^':
            dr = -1

        case 'v':
            dr = 1

    if warehouse[botRow+dr][botCol+dc] == '#':
        return (botRow, botCol)
    
    if warehouse[botRow+dr][botCol+dc] == '.':
        warehouse[botRow+dr][botCol+dc] = '@'
        warehouse[botRow][botCol] = '.'
        return (botRow+dr, botCol+dc)
    
    if dr != 0:
        if warehouse[botRow+dr][botCol] == '[':
            if moveBoxVertical(warehouse, botRow+dr, botCol, dr):
                warehouse[botRow+dr][botCol+dc] = '@'
                warehouse[botRow][botCol] = '.'
                return (botRow+dr, botCol+dc)
        else:
            if moveBoxVertical(warehouse, botRow+dr, botCol-1, dr):
                warehouse[botRow+dr][botCol+dc] = '@'
                warehouse[botRow][botCol] = '.'
                return (botRow+dr, botCol+dc)
    elif dc == -1:
        if moveBoxLeft(warehouse, botRow, botCol-2):
            warehouse[botRow+dr][botCol+dc] = '@'
            warehouse[botRow][botCol] = '.'
            return (botRow+dr, botCol+dc)
    elif dc == 1:
        if moveBoxRight(warehouse, botRow, botCol+1):
            warehouse[botRow+dr][botCol+dc] = '@'
            warehouse[botRow][botCol] = '.'
            return (botRow+dr, botCol+dc)
    
    return (botRow, botCol)

def calcuateSumOfGPS(layout: list[list[str]], box: str) -> int:
    total = 0

    for r, row in enumerate(warehouse):
        for c, marker in enumerate(row):
            if marker == box:
                total += 100 * r + c

    return total

# Script

with open('15.txt') as f:
    text = f.read()

layout, moves = text.split('\n\n')

warehouse = [list(row) for row in layout.split('\n')]

wideWarehouse = []
wideWarehouse = []
for row in layout.split('\n'):
    newRow = []
    for space in row:
        match space:
            case 'O':
                newRow.extend(['[', ']'])
            case '@':
                newRow.extend(['@', '.'])
            case _:
                newRow.extend([space, space])
    wideWarehouse.append(newRow)

# Part 1

for r, row in enumerate(warehouse):
    if '@' in row:
        bot = (r, row.index('@'))
        row[bot[1]] = '.'

moves = ''.join(moves.split('\n'))

for m in moves:
    bot = move(warehouse, bot, m)

print(calcuateSumOfGPS(warehouse, 'O'))

# Part 2

warehouse = wideWarehouse

for r, row in enumerate(warehouse):
    if '@' in row:
        botRow = r
        botCol = row.index('@')

moves = ''.join(moves.split('\n'))

for move in moves:
    botRow, botCol = moveBot(warehouse, botRow, botCol, move)

print(calcuateSumOfGPS(warehouse, '['))