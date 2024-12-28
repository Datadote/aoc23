import math
from aocd import get_data
inp = get_data(day=3, year=2023)

def find_numbers_in_line(line):
    starts = []
    ends = []
    new_num = True
    for i, c in enumerate(line):
        if c.isdigit() and new_num:
            starts.append(i)
            new_num = False
        elif not c.isdigit() and not new_num:
            ends.append(i)
            new_num = True
    if not new_num:
        ends.append(i+1)
    numbers = [line[s:e] for s,e in zip(starts, ends)]
    return numbers, starts, ends

def any_punc(line, s_idx, e_idx):
    return any(not c.isdigit() and c != '.' for c in line[s_idx:e_idx])

def is_valid(grid, line_num, start, end):
    is_valid = False
    s_idx = start-1 if start-1 >= 0 else 0
    e_idx = end+1 if end+1 < len(grid[line_num]) else len(grid[line_num])
    
    if line_num - 1 >= 0:
        is_valid |= any_punc(grid[line_num - 1], s_idx, e_idx)
    is_valid |= any_punc(grid[line_num], s_idx, e_idx)
    if line_num + 1 < len(grid):
        is_valid |= any_punc(grid[line_num + 1], s_idx, e_idx)
    return is_valid

grid = inp.split('\n')
res = 0
for i in range(len(grid)):
    total = 0
    numbers, starts, ends = find_numbers_in_line(grid[i])
    for n, s, e in zip(numbers, starts, ends):
        if is_valid(grid, i, s, e):
            total += int(n)
    res += total
print(f"Final total sum: {res}")