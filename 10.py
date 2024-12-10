def search(row: int, col: int, nextHeight:int, graph: list[list[int]], foundPeaks: set) -> int:
    if nextHeight == 10:
        foundPeaks.add((row, col))
        return 1
    
    foundPaths = 0

    if row - 1 > -1 and graph[row-1][col] == nextHeight:
        foundPaths += search(row-1, col, nextHeight+1, graph, foundPeaks)
    if row + 1 < len(graph) and graph[row+1][col] == nextHeight:
        foundPaths += search(row+1, col, nextHeight+1, graph, foundPeaks)
    if col - 1 > -1 and graph[row][col-1] == nextHeight:
        foundPaths += search(row, col-1, nextHeight+1, graph, foundPeaks)
    if col + 1 < len(graph[0]) and graph[row][col+1] == nextHeight:
        foundPaths += search(row, col+1, nextHeight+1, graph, foundPeaks)
    
    return foundPaths

with open('10.txt', mode='r') as f:
    text = f.read()

rows = text.split('\n')
graph = []
for r in rows:
    graph.append(list(map(int, r)))

p1Total = 0
p2Total = 0
for r, row in enumerate(graph):
    for c, height in enumerate(row):
        if height == 0:
            foundPeaks = set()
            p2Total += search(r, c, 1, graph, foundPeaks)
            p1Total += len(foundPeaks)

print(p1Total)
print(p2Total)
