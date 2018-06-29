def contains(list_of_integers, x):
    ceiling = len(list_of_integers)
    floor = -1
    while floor+1 < ceiling:
        d = ceiling - floor
        half_distance = d/2
        mid = floor + half_distance
        if list_of_integers[mid] == x:
            return True
        if list_of_integers[mid] > x:
            ceiling = mid
        else:
            floor = mid
    return False

