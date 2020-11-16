import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

#print(list(gen_random(random.randint(2,5),random.randint(0,10),random.randint(10,100))))