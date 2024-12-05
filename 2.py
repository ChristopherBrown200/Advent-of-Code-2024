# Part 1
with open('2.txt') as f:
    text = f.read()
    lines = text.split('\n')


total = 0

for l in lines:
    level = list(map(int, l.split()))
    if level == sorted(level) or level == sorted(level, reverse=True):
        add = 1
        for i in range(0, len(level)-1):
            if abs(level[i] - level[i+1]) > 3 or abs(level[i] - level[i+1]) == 0:
                add = 0
                break
        print(level, add)
        total += add

print (total)

# Part 2
def check(level):
    safe = False
    if level == sorted(level) or level == sorted(level, reverse=True):
        safe = True

        for i in range(0, len(level)-1):
            if abs(level[i] - level[i+1]) > 3 or abs(level[i] - level[i+1]) == 0:
                safe = False
                break
    return safe

with open('2.txt') as f:
    text = f.read()
    lines = text.split('\n')


total = 0

for l in lines:
    level = list(map(int, l.split()))
    if check(level):
        total += 1
    else:
        for i in range(len(level)):
            newLevel = level.copy()
            del newLevel[i]
            if check(newLevel):
                total += 1
                print(level)
                break

print (total)