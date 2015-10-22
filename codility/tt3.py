__author__ = 'tanchao@github'

def sample(A):
    north, east, south, west = 0, 0, 0, 0
    x, y = 0, 0  # init position
    res = 0
    for i, v in enumerate(A):
        direction = i % 4
        if direction == 0:  # move north
            if x == 0 and y == 0:  # initial
                y += v
            else:
                if x >= west and x <= east and y + v >= north:  # cross north edge
                    res = i + 1
                    break
                else:
                    y += v
                    if north < y:
                        north = y
        if direction == 1:
            if y <= north and y >=south and x + v >= east:  # cross east edge
                res = i + 1
                break
            else:
                x += v
                if east < x:
                    east = x
        if direction == 2:
            if x >= west and x <= east and y + v <= south:  # cross south edge
                res = i + 1
                break
            else:
                y += v
                if south > y:
                    south = y
        if direction == 3:
            if y <= north and y >=south and x + v <= west:  # cross west edge
                res = i + 1
                break
            else:
                x += v
                if west > x:
                    west = x
        return res

if __name__ == '__main__':
    sample([1,3,2,5,4,4,6,3,2])
