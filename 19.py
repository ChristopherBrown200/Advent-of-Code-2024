towelsByFirstLetter = {
    'w' : [],
    'u' : [],
    'b' : [],
    'r' : [],
    'g' : [],
}

possiblePattens = dict()

def checkPatternPossible(pattern: str) -> int:
    for t in towels:
        if pattern.find(t) == 0:
            if t == pattern:
                return 1
            elif checkPatternPossible(pattern.removeprefix(t)) == 1:
                return 1
    return 0

def checkTimesPatternPossible(pattern: str) -> int:
    count = 0
    if pattern in possiblePattens:
        count = possiblePattens[pattern]
    else:
        for t in towelsByFirstLetter[pattern[0]]:
            if pattern.find(t) == 0:
                if t == pattern:
                    count += 1
                else :
                    count += checkTimesPatternPossible(pattern.removeprefix(t))
        possiblePattens[pattern] = count
    return count

with open('19.txt') as f:
    text = f.read()
towels, patterns = text.split('\n\n')
towels = towels.split(', ')
patterns = patterns.split('\n')
for t in towels:
    towelsByFirstLetter[t[0]].append(t)

print(sum(checkPatternPossible(p) for p in patterns))
print(sum(checkTimesPatternPossible(p) for p in patterns))
