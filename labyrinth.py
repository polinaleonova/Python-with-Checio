def find_path(labyrinth):
    '''
    :param labyrinth: list 12x12 like   [[1,1,1,1,1,1,1,1,1,1,1,1],
                                 [1,0,1,0,0,0,1,0,0,0,0,1],
                                 [1,0,1,0,1,0,1,0,1,1,0,1],
                                 [1,0,1,0,1,0,1,0,1,0,0,1],
                                 [1,0,1,0,1,0,1,0,1,0,1,1],
                                 [1,0,1,0,1,0,1,0,1,0,0,1],
                                 [1,0,1,0,1,0,1,0,1,1,0,1],
                                 [1,0,1,0,1,0,1,0,1,0,0,1],
                                 [1,0,1,0,1,0,1,0,1,0,1,1],
                                 [1,0,1,0,1,0,1,0,1,0,0,1],
                                 [1,0,0,0,1,0,0,0,1,1,0,1],
                                 [1,1,1,1,1,1,1,1,1,1,1,1]]
    :return:list of tuples with path's coordinates. example [(1,1),(1,2),(1,3),(2,3),(3,3)]
    '''
    all_path = [[(1, 1)]]
    for path in all_path:
        x = path[-1][0]
        y = path[-1][1]
        if labyrinth[y-1][x] == 0:
            new_path = path[::]
            new_path.append((x, y-1))
            all_path.append(new_path)
        if labyrinth[y+1][x] == 0:
            new_path = path[::]
            new_path.append((x, y+1))
            all_path.append(new_path)
        if labyrinth[y][x-1] == 0:
            new_path = path[::]
            new_path.append((x-1, y))
            all_path.append(new_path)
        if labyrinth[y][x+1] == 0:
            new_path = path[::]
            new_path.append((x+1, y))
            all_path.append(new_path)
        if x == 10 and y == 10:
            return path
        labyrinth[y][x] = 1


def checkio(labyrinth):
    '''
    :param labyrinth: list 12x12 like [[1,1,1,1,1,1,1,1,1,1,1,1],
                                     [1,0,1,0,0,0,1,0,0,0,0,1],
                                     [1,0,1,0,1,0,1,0,1,1,0,1],
                                     [1,0,1,0,1,0,1,0,1,0,0,1],
                                     [1,0,1,0,1,0,1,0,1,0,1,1],
                                     [1,0,1,0,1,0,1,0,1,0,0,1],
                                     [1,0,1,0,1,0,1,0,1,1,0,1],
                                     [1,0,1,0,1,0,1,0,1,0,0,1],
                                     [1,0,1,0,1,0,1,0,1,0,1,1],
                                     [1,0,1,0,1,0,1,0,1,0,0,1],
                                     [1,0,0,0,1,0,0,0,1,1,0,1],
                                     [1,1,1,1,1,1,1,1,1,1,1,1]]
    It is a map of labyrinth where 0 - road, 1 - bush;
    Outer walls always must be 1;
    len(labyrinth) == 12;
    all(len(row) == 12 for row in labyrinth);
    :return: string with first letters of direction ('N' -if north,'E' - if east, ...)
     from start point (1,1) to end (10,10)
    '''
    path = find_path(labyrinth)
    way = ''
    n = len(path)
    for x in range(n-1):
        if path[x][0] < path[x+1][0]:
            way += 'E'
        if path[x][1] < path[x+1][1]:
            way += 'S'
        if path[x][0] > path[x+1][0]:
            way += 'W'
        if path[x][1] > path[x+1][1]:
            way += 'N'
    return way
