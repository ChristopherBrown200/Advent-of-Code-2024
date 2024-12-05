def checkCommand(t: str) -> int:
    if t.find(',') != -1 and t.find(')') != -1:
        n1 = t[:t.find(',')]
        n2 = t[t.find(',')+1:t.find(')')]
        if n1.isnumeric() and n2.isnumeric():
            return int(n1) * int(n2)
    return 0

def processChunk(chunk: str) -> int:
    return sum(checkCommand(command) for command in chunk.split('mul('))

with open('3.txt') as f:
    text = f.read()

# Part 1
print(processChunk(text))

# Part 2
def processIfValid(chunk: str) -> int:
    if chunk.find('do()') != -1:
        return processChunk(chunk[chunk.find('do()')+4:])
    return 0

total = 0
print(sum(processIfValid(chunk) for chunk in ('do()' + text).split("don't()")))

