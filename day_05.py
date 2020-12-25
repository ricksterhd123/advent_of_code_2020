import math
import re

def get_row(b):
    l = 0
    r = 127
    for c in b:
        if c == 'F':
            r = math.floor((r+l)/2)
        elif c == 'B':
            l = math.ceil((r+l)/2)
    return math.floor((l + r) / 2)

def get_column(b):
    l = 0
    r = 7
    for c in b:
        if c == 'L':
            r = math.floor((r+l)/2)
        elif c == 'R': 
            l = math.ceil((r+l)/2)
    return math.floor((l + r) / 2)

def get_seat_ID(row, col):
    return row * 8 + col

def split_boarding(bstring):
    m = re.match('((F|B){7})((L|R){3})', bstring)
    if m:
        return m.group(1), m.group(3)
    else:
        return False

if __name__ == '__main__':
    highest_id = 0
    with open('day_05.txt') as f:
        lines = f.read().split('\n')
        for line in lines:
            rowstr, colstr = split_boarding(line)
            if rowstr:
                id = get_seat_ID(get_row(rowstr), get_column(colstr))
                if highest_id < id:
                    highest_id = id
    print(highest_id)