


def get_num_paths(width):
    lattices = [[1]*width,]
    
    for i in range(1,width):
        lattices.append([1,])

    for x in range(1, width):
        for y in range(1, width):
            new_lattice = lattices[y-1][x] + lattices[y][x-1]
            lattices[y].append(new_lattice)

    print(lattices)
    return lattices[width-1][width-1]
        
print(get_num_paths(21))
