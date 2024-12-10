def findNth(string: str, subString: str, n: int):
    val = -1
    for _ in range(0, n):
        val = string.find(subString, val+1)
    return val

with open('9.txt', mode='r') as f:
    text = f.read().strip()

map = list(map(int, list(text)))

# Part 1

s = []
for i, num in enumerate(map):
    if i % 2 == 0:
        for _ in range(num):
            s.append(int(i/2))
    else:
        for _ in range(num):
            s.append('.')

blank = s.index('.')

for i in range(len(s)-1, -1, -1):
    if blank > i:
        break

    if s[i] != '.':
        s[blank] = s[i]
        s[i] = '.'
        blank = s.index('.')

total = 0

for i, num in enumerate(s):
    if num == '.':
        break
    total += i*num

print(total)

# Part 2
s = []
for i, num in enumerate(map):
    if i % 2 == 0:
        for _ in range(num):
            s.append(int(i/2))
    else:
        for _ in range(num):
            s.append('.')

endNum = s[-1]

for num in range(endNum, 0, -1):
    numCount = s.count(num)
    if numCount == 0:
        continue

    dotCount = 0
    dotStart = -1

    for i, place in enumerate(s):
        if place == num:
            dotStart = -1
            break
        if place == '.':
            if dotCount > 0:
                dotCount += 1
            else:
                dotStart = i
                dotCount = 1
            if dotCount >= numCount:
                break
        else:
            dotCount = 0
    
    if dotStart != -1 and dotCount >= numCount:
        while num in s:
            index = s.index(num)
            s[index] = '.'
        for i in range(dotStart, dotStart + numCount):
            s[i] = num

total = 0
for i, place in enumerate(s):
    if place != '.':
        total += i * place
print(total)

