# decided to use python because it is quicker...

import os
import re

def list_policies(path):
    result = []
    with open(path, 'r') as f:
        for line in f.read().rsplit('\n'):
            m = re.match('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
            result.append([int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)])
    return result

def policy1(x):
    return x[0] <= x[3].count(x[2]) <= x[1]

def policy2(x):
    return (x[3][x[0]-1] == x[2]) != (x[3][x[1]-1] == x[2])

if __name__ == "__main__":
    counta = 0
    countb = 0
    for x in list_policies('day_02.txt'):
        if policy1(x):
            counta += 1
        if policy2(x):
            countb += 1

    print(counta, countb)
