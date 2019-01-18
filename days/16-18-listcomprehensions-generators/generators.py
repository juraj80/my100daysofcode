import random, itertools

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

title_case =[name.title() for name in NAMES]
print(title_case)

def reverse_first_last_names(name):
    first,last = name.split()
    # ' '.join([last,first]) -- wait we have f-strings now (>= 3.6)
    return f'{last} {first}'

reversed = [reverse_first_last_names(name) for name in NAMES]

print(reversed)


def gen_pairs():
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        first,second = None, None
        while first == second:
            first, second = random.sample(first_names,2)
        yield f'{first} teams up with {second}'

pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))

first_ten = itertools.islice(pairs,10)
print(list(first_ten))
