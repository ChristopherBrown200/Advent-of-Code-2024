def checkForNextChar(lines: list[str], char: str, line: int, index:int) -> bool:
    return lines[line][index] == char

def checkForXMAS(lines: list[str], intialL: int, intialC: int, offesetL: int, offsetC: int) -> bool:
    try:
        if checkForNextChar(lines, 'M', intialL+offesetL, intialC+offsetC):
            if checkForNextChar(lines, 'A', intialL+(offesetL*2), intialC+(offsetC*2)):
                if checkForNextChar(lines, 'S', intialL+(offesetL*3), intialC+(offsetC*3)) and intialL+(offesetL*3) > -1 and intialC+(offsetC*3) > -1:
                    return True
    except:
        pass
    return False
        

def CheckForX(lines: list[str], line: int, char: int) -> bool:
    if line == 0 or line == len(lines)-1 or char == 0 or char == len(lines[line])-1:
        return False
    
    topLeft = lines[line-1][char-1]
    topRight = lines[line-1][char+1]
    bottomLeft = lines[line+1][char-1]
    bottomRight = lines[line+1][char+1]

    v = 'MS'

    if topLeft != bottomRight and topRight != bottomLeft and topLeft in v and topRight in v and bottomLeft in v and bottomRight in v:
        return True
    return False

with open('4.txt') as f:
    text = f.read()

# Part 1
lines = text.split('\n')

total = 0

for l, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == 'X':
            for lOffset in range(-1, 2):
                for cOffset in range(-1, 2):
                    if checkForXMAS(lines, l, c, lOffset, cOffset):
                        total += 1
print(total)

# Part 2
lines = text.split('\n')

total = 0

for l, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == 'A':
            if CheckForX(lines, l, c):
                total += 1

print(total)
