from collections import Counter

with open('11.txt') as f:
    stones = list(map(int, f.read().strip().split()))


def countStones(stones: list[int], blinks: int) -> int:
    stones = Counter(stones)
    for _ in range(blinks):
        newStones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                newStones[1] += count
            else:
                string = str(stone)
                l = len(string)
                if l % 2 == 0:
                    newStones[int(string[:l//2])] += count
                    newStones[int(string[l//2:])] += count
                else:
                    newStones[stone*2024] += count
        stones = newStones
    return sum(stones.values())

# Part 1
print(countStones(stones, 25))
# Part 2
print(countStones(stones, 75))