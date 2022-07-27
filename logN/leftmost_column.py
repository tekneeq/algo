

#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

'''
grid
[[0,0],[1,1]]
dimensions()
[2,2]
'''

def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

    # leftmost column where not all 0s
    # iterate by columns and find the first 1
    max_row, max_col = binaryMatrix.dimensions()


    def check_col(col):
        # returns True of col has a 1
        # else returns False

        has_one = False
        for row in range(max_row):
            if binaryMatrix.get(row, col) == 1:
                has_one = True
                break

        return has_one

    low_col, high_col = (0, max_col -1)
    # [
    #   [0,    0],
    #   [1,    1]
    # ]

    # iteration one: mid_col = 1//2 == 0
    # iteration two: exit because high_col == -1

    last_col_with_one = -1
    while low_col <= high_col:
        mid_col = (low_col + high_col) // 2


        if check_col(mid_col):
            # found one so check left side
            last_col_with_one = mid_col
            high_col = mid_col - 1
        else:
            # not found so check right side
            low_col = mid_col + 1

    return last_col_with_one