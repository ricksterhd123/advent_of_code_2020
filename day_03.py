if __name__ == "__main__":
    with open('day_03.txt') as f:
        lines = f.read().split('\n')

    # part A
    trees = 0
    x = 0
    for y in range(1, len(lines), 1):
            track = lines[y]
            x = (x + 3) % len(track) 
            if (track[x] == '#'):
                trees += 1
    print(trees)
    
    # part B
    product = 1
    for slopes in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
        trees = 0
        x = 0
        for y in range(slopes[1], len(lines), slopes[1]):
            track = lines[y]
            x = (x + slopes[0]) % len(track) 
            if (track[x] == '#'):
                trees += 1
        product *= trees
    print(product)