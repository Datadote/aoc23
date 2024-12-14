from aocd import get_data
inp = get_data(day=2, year=2023)

lines = inp.splitlines()
lines = [line.split(': ')[1:] for line in lines]
lines = [line[0].split(';') for line in lines]
total = 0
dmax = {'red': 12, 'green': 13, 'blue': 14}
d = {}
for i, game in enumerate(lines):
    good = True
    for roll in game:
        roll = roll.split(',')
        for cubes in roll:
            cubes = cubes.strip()
            cubes = cubes.split()
            num, color = int(cubes[0]), cubes[1]
            if num > dmax[color]:
                good = False
    if good:
        total += 1 + i
print(total)