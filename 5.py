toBeFixed = []

# Part 1
def checkPrevPages(update:str, p:int, page:str, rules:dict) -> bool:
    if page not in rules:
        return True

    notAllowed = rules[page]
    for i in range(p-1, -1, -1):
        if update[i] in notAllowed:
            return False
    return True

def checkUpdate(update:str, rules:dict) -> int:
    for p, page in enumerate(update):
        if not checkPrevPages(update, p, page, rules):
            toBeFixed.append(update)
            return 0
    return int(update[int((len(update)-1)/2)])

rules = dict()
updates = []

with open('5.txt') as f:
    while True:
        rule = f.readline().strip()
        if '|' not in rule:
            break
        a, b = rule.split('|')
        if a in rules:
            rules[a].append(b)
        else: 
            rules[a] = [b]

    rUpdates = f.read().split('\n')
    for rU in rUpdates:
        updates.append(rU.split(','))
    
print(sum(checkUpdate(update, rules) for update in updates))

# Part 2
def fixUpdate(update:list, rules: dict) -> int:
    for p, page in enumerate(update):
        newIndex = p
        while not checkPrevPages(update, newIndex, page, rules):
            newIndex -= 1
        del update[p]
        update.insert(newIndex, page)
    return int(update[int((len(update)-1)/2)])


print(sum(fixUpdate(update, rules) for update in toBeFixed))