from typing import List


def findBall(grid: List[List[int]]) -> List[int]:
    column_limit = len(grid[0])  # -1
    row_limit = (len(grid))  # -1
    answer = []

    # while we have not reached the limit
    for index in range(column_limit):
        # start at the first row, and the current column
        cur_col, cur_row = index, 0
        # set default value for the final column
        column_final = -1
        # TODO: try with just one column, the first for now, then decide if we use another for each
        while cur_col < column_limit and cur_row < row_limit:
            # get current cell
            cur_cel = grid[cur_row][cur_col]
            # check the current value of the cell
            # TODO: simplify with one section for both 1, -1
            if cur_cel == 1:
                # expect the immediate next column to be in the same direction
                next_column = cur_col + 1 if cur_col + 1 < column_limit else None
                next_column_val = grid[cur_row][next_column] if next_column else None
                # check the next row of the path
                if next_column_val == cur_cel:
                    # go to the column being signaled
                    cur_col += 1
                    # go to the next row
                    cur_row += 1
                # end path
                else:
                    break

            if cur_cel == -1:
                # expect the immediate next column to be in the same direction
                next_column = cur_col - 1 if cur_col - 1 >= 0 else None
                next_column_val = grid[cur_row][next_column] if next_column is not None else None
                # check the next row of the path
                if next_column_val == cur_cel:
                    # go to the column being signaled
                    cur_col -= 1
                    # go to the next row
                    cur_row += 1
                # end path
                else:
                    break

            # check if the column is out of boundaries
            if cur_col < 0 or cur_col > column_limit:
                # if we have reached the row limit, return the column
                if cur_row > row_limit:
                    column_final = cur_col

                # else, "null" value
                else:
                    break

            if cur_row >= row_limit:
                column_final = cur_col
        # append result to the answer
        answer.append(column_final)
    # out
    return answer


if __name__ == '__main__':
    # example 1
    findBall(grid=[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1],
                   [-1, -1, -1, -1, -1]])  # [1,-1,-1,-1,-1]
    # example 2
    findBall([[-1]])  # -1
    # example 3
    findBall(grid=[[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1],
                   [-1, -1, -1, -1, -1, -1]])  # [0,1,2,3,4,-1]

    # example 4
    findBall(grid=[[1, 1, 1], [1, 1, 1], [-1, -1, -1]])



