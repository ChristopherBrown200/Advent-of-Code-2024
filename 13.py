with open('13.txt') as f:
    text = f.read()

text = text.split('\n\n')

machines = []
for t in text:
    machines.append(t.split('\n'))

totalCostP1 = 0
totalCostP2 = 0

for m in machines:
    x1 = int(m[0][m[0].find('X+')+1: m[0].find(',')])
    y1 = int(m[0][m[0].find('Y+')+1:])

    x2 = int(m[1][m[1].find('X+')+1: m[1].find(',')])
    y2 = int(m[1][m[1].find('Y+')+1:])

    xt = int(m[2][m[2].find('X=')+2: m[2].find(',')])
    yt = int(m[2][m[2].find('Y=')+2:])
    
    # Part 1
    B = ((x1*yt)-(xt*y1)) / ((x1*y2)-(y1*x2))
    A = (xt-(x2*B))/x1
    if A.is_integer() and B.is_integer():
        totalCostP1 += int(A*3 + B)

    # Part 2
    xt += 10000000000000
    yt += 10000000000000
    B = ((x1*yt)-(xt*y1)) / ((x1*y2)-(y1*x2))
    A = (xt-(x2*B))/x1
    if A.is_integer() and B.is_integer():
        totalCostP2 += int(A*3 + B)

print(totalCostP1)
print(totalCostP2)