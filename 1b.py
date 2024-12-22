from aocd import get_data
inp = get_data(day=1, year=2023)

nums = {str(i): i for i in range(10)}
number_words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0
}
number_words = {**nums, **number_words}

def get_num(s):
    first, last = None, None
    for i in range(len(s)):
        for k, v in number_words.items():
            if s[i:].startswith(k):
                if first is None:
                    first = number_words[k]
                last = number_words[k]
    return 10 * first + last

lines = inp.splitlines()  
total = sum(get_num(s) for s in lines)
print(total)