import math
from aocd import get_data
inp = get_data(day=2, year=2023)

lines = inp.splitlines()
lines = [line.split(': ')[1:] for line in lines]
lines = [line[0].split(';') for line in lines]
total = 0
for game in lines:
    dmax = {'red': 0, 'green': 0, 'blue': 0}
    for roll in game:
        roll = roll.split(',')
        for cubes in roll:
            cubes = cubes.strip()
            cubes = cubes.split()
            num, color = int(cubes[0]), cubes[1]
            dmax[color] = max(dmax[color], num)
    total += math.prod(dmax.values())
print(total)