# Part 1
list1 = []
list2 = []

with open('1.txt', mode='r') as f:
    for _ in range(1000):
        a, b = map(int, f.readline().strip().split())
        list1.append(a)
        list2.append(b)

list1.sort()
list2.sort()

total = 0
for i in range(1000):
    total += abs(list1[i] - list2[i])

print(total)

# Part 2
left = []
right = dict()

with open('1.txt', mode='r') as f:
    for _ in range(1000):
        a, b = map(int, f.readline().strip().split())
        left.append(a)
        
        if b in right:
            right[b] += 1
        else:
            right[b] = 1

total = 0

for n in left:
    if n in right:
        total += (right[n] * n)

print(total)