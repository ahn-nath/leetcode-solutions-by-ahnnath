from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    minutes_count = 0

    # find all rotten oranges
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            cell = grid[row][column]
            # if the current cell is healthy or empty, skip
            if 1 == cell or 0 == cell:
                continue
            # else, if current cell is healthy (1), check if the adjacent cells are rotten
            else:
                # check the top
                top = grid[row - 1][column] if row > 0 else 0
                # check the bottom
                bottom = grid[row + 1][column] if row < (len(grid) - 1) else 0
                # check the left
                left = grid[row][column - 1] if column > 0 else 0
                # check the right
                right = grid[row][column + 1] if column < (len(grid[0]) - 1) else 0

                # if any of the adjacent cells are rotten, rot the current cell
                if top == 1 or bottom == 1 or left == 1 or right == 1:
                    # mark the current orange as rotten
                    # grid[row][column] = 2

                    if top == 1:
                        # mark top as rotten
                        grid[row - 1][column] = 2
                    if bottom == 1:
                        # mark bottom as rotten
                        grid[row + 1][column] = 2
                    if left == 1:
                        # mark left as rotten
                        grid[row][column - 1] = 2
                    if right == 1:
                        # mark right as rotten
                        grid[row][column + 1] = 2

                    # increment count
                    minutes_count += 1

    for row in grid:
        # if any in current group is 1 after this row iteration, return -1
        if 1 in row:
            print(-1)
            print(grid)
            return -1

    print(minutes_count)
    print(grid)
    return minutes_count


if __name__ == '__main__':
    orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]])  # 4

    orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]])  # -1

    orangesRotting(grid=[[0, 2]])  # 0

    orangesRotting(grid=
                   [[1], [2]])
