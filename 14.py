with open('14.txt') as f:
    text = f.read()

robots = text.split('\n')

width = 101
height = 103

# Part 1
midCol = width//2
midRow = height//2

quads = [0, 0, 0, 0]

for bot in robots:
    p, v = bot.split()
    p = (int(p[2:p.find(',')]), int(p[p.find(',')+1:]))
    v = (int(v[2:v.find(',')]), int(v[v.find(',')+1:]))

    col = (p[0] + v[0] * 100) % width
    row = (p[1] + v[1] * 100) % height

    if row > midRow and col > midCol:
        quads[0] += 1
    elif row > midRow and col < midCol:
        quads[1] += 1
    elif row < midRow and col > midCol:
        quads[2] += 1
    elif row < midRow and col < midCol:
        quads[3] += 1

print(quads[0] * quads[1] * quads[2] * quads[3])

# Part 2
count = 0
sharing = True
while(sharing):
    count += 1
    locations = set()
    for bot in robots:
        p, v = bot.split()
        p = (int(p[2:p.find(',')]), int(p[p.find(',')+1:]))
        v = (int(v[2:v.find(',')]), int(v[v.find(',')+1:]))

        col = (p[0] + v[0] * count) % width
        row = (p[1] + v[1] * count) % height

        if (row, col) in locations:
            sharing = True
            break
        locations.add((row, col))
        sharing = False
print(count)

