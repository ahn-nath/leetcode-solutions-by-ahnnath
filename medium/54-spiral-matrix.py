from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # order should be:
    # top --> right.
    # right --> bottom.
    # bottom --> left.
    # left --> top.

    # initialize variables
    direction = 2  # directions  can be: 1 [top], 2 [right], 3 [bottom], 4 [left]
    row, column = 0, -1
    limit_row, limit_column = len(matrix), len(matrix[0])
    limit = limit_column

    # output
    spiral_output = []

    while limit_row and limit_column > 0:
        count = 0
        while count < limit:
            # decide action based on direction status
            # if [top], keep increasing the row value, at column position
            if direction == 1:
                row -= 1
            # if [right], keep increasing the column value at row position
            if direction == 2:
                column += 1
            # if [bottom], keep decreasing the row value at column position
            if direction == 3:
                row += 1
            # if [left], keep decreasing the column value at row position
            if direction == 4:
                column -= 1

            # update output and count
            spiral_output.append(matrix[row][column])

            count += 1

        # update availability of row or column based on direction
        # if direction was horizontal, update row availability
        if direction in (2, 4):
            limit_row -= 1
            # update limit to the next direction in dimension
            limit = limit_row
        # if direction was vertical, update column availability
        if direction in (1, 3):
            limit_column -= 1
            # update limit to the next direction in dimension
            limit = limit_column

        # change direction
        direction = (direction + 1) if (direction < 4) else 1

    return spiral_output


if __name__ == '__main__':
    print(spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
    print(spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
