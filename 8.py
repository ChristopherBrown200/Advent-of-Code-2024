with open('8.txt', mode='r') as f:
    text = f.read()

# Part 1
rows = text.split('\n')
map = []
for r in rows:
    map.append(list(r))

numRow = len(map)
numCol = len(map[0])

antennas = dict()
antinodes = set()

for r, row in enumerate(map):
    for c, char in enumerate(row):
        if char != '.':
            if char not in antennas:
                antennas[char] = [(r,c)]
            else:
                antennas[char].append((r,c))

for a in antennas:
    if len(antennas[a]) == 1:
        continue

    for loc1 in antennas[a]:
        for loc2 in antennas[a]:
            if loc1 == loc2:
                continue

            dr = loc1[0] - loc2[0]
            dc = loc1[1] - loc2[1]
            possAntiR = loc2[0] - dr
            possAntiC = loc2[1] - dc

            if possAntiR < 0 or possAntiR >= numRow or possAntiC < 0 or possAntiC >= numCol:
                continue

            antinodes.add((possAntiR, possAntiC))

print(len(antinodes))

# part 2
antinodes.clear()
for a in antennas:
    if len(antennas[a]) == 1:
        continue

    for loc1 in antennas[a]:
        antinodes.add(loc1)
        for loc2 in antennas[a]:
            if loc1 == loc2:
                continue

            dr = loc1[0] - loc2[0]
            dc = loc1[1] - loc2[1]
            possAntiR = loc2[0] - dr
            possAntiC = loc2[1] - dc

            while possAntiR > -1 and possAntiR < numRow and possAntiC > -1 and possAntiC < numCol:
                antinodes.add((possAntiR, possAntiC))

                possAntiR -= dr
                possAntiC -= dc

print(len(antinodes))