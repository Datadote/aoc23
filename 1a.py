from aocd import get_data
inp = get_data(day=1, year=2023)

def get_num(s):
    first, last = None, None
    for c in s:
        if c.isdigit():
            if first is None:
                first = int(c)
            last = int(c)
    return 10 * first + last

lines = inp.splitlines()  
total = sum(get_num(s) for s in lines)
print(total)