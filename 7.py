import itertools

with open('7.txt', mode='r') as f:
    text = f.read()

# Part 1
total = 0

equations = text.split('\n')
for e in equations:
    testValue, nums = e.split(':')
    testValue = int(testValue)
    nums = list(map(int, nums.split()))

    possibleOps = list(itertools.product([1,0], repeat=len(nums)-1))

    for op in possibleOps:
        check = nums[0]
        for i, op in enumerate(op):
            if op != 0:
                check += nums[i+1]
            else:
                check *= nums[i+1]

        if check == testValue:
            total += testValue
            break
print(total)


# Part 2
total = 0

equations = text.split('\n')
for e in equations:
    testValue, nums = e.split(':')
    testValue = int(testValue)
    nums = list(map(int, nums.split()))

    possibleOps = list(itertools.product([2,1,0], repeat=len(nums)-1))

    for op in possibleOps:
        check = nums[0]
        for i, op in enumerate(op):
            if op == 0:
                check += nums[i+1]
            elif op == 1:
                check *= nums[i+1]
            else:
                check = int(f'{check}{nums[i+1]}')

        if check == testValue:
            total += testValue
            break
print(total)

