# -*- coding: utf8 -*-

def checkio(map):

    """
    :param map: string is relation between numbers, example "12,23,34,45,56,67,78,81"
    :return: string as path through all numbers, start and finish in "1"
    """
    # get from string map list of strings and there reverse variants
    from itertools import chain
    map_list = list(chain.from_iterable((i, i[::-1]) for i in map.split(",")))
    relations = {}
    # write to dict relations key - string with number, value - list of strings
    #which related with this number
    for item in map_list:
        if item[0] in relations.keys():
            relations[item[0]].append(item[1])
        else:
            relations[item[0]] = list(item[1])
    # create list with start routes
    routes = [start_route for start_route in map_list if start_route[0] == "1"]
    for route in routes:
        for val in relations[route[-1]]:
            if val != route[-2]:
                temp_route = route[::]
                temp_route = temp_route + val
                if temp_route[-1] == "1" and len(set(temp_route)) == 8:
                        return temp_route
                routes.append(temp_route) #add to current route new point
        del route

# print checkio("12,13,14,15,16,17,18,82,83,84,85,86,87")
# print checkio("12,23,34,45,56,67,78,81")
# print checkio("12,28,87,71,13,14,34,35,45,46,63,65")
# print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")
# print checkio("13,14,23,25,34,35,47,56,58,76,68")
