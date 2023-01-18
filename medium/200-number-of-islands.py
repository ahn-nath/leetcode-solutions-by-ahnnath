from typing import List


def numIslands(grid: List[List[str]]) -> int:
    # if not empty
    if not grid:
        return 0

    islands = 0
    nexti = (0, 0)
    r_limit = len(grid)
    c_limit = len(grid[0])
    while nexti:
        er, ec = nexti
        # check if current cell is a land
        print(f'sr: {er}, sc: {ec}')
        if grid[er][ec] == '1':
            # iterate over array to check for position having a land (1)
            stack = {nexti}
            while stack:
                curr = stack.pop()
                sr, sc = curr

                # mark as 2
                grid[sr][sc] = 2
                # handle children
                left = grid[sr][sc - 1] if sc - 1 >= 0 else None
                right = grid[sr][sc + 1] if sc + 1 < c_limit else None
                top = grid[sr - 1][sc] if sr - 1 >= 0 else None
                bottom = grid[sr + 1][sc] if sr + 1 < r_limit else None

                # check if adjacent pixels are present (top, bottom, left, right)
                if top == '1':
                    stack.add((sr - 1, sc))
                if bottom == '1':
                    stack.add((sr + 1, sc))
                if left == '1':
                    stack.add((sr, sc - 1))
                if right == '1':
                    stack.add((sr, sc + 1))
            # when we get to the second loop, redefine er and ec
            # TODO: add the next number (column) because we know is likely empty, else next row
            '''
            # Removing as of now to verify previous columns
            # ec = sc + 1 if sc+1 < c_limit else 0 # else first column
            # er = sr+1 if ec == 0 and sr+1 < r_limit else sr # else keep it simple because it is the same row but different column
            '''

            # count island
            islands += 1
        # define next node/cell
        # check cell in the next column, if not last column
        if ec + 1 < c_limit:
            nexti = (er, ec + 1)
        # check first cell in the next row, if not last row
        elif er + 1 < r_limit:
            nexti = (er + 1, 0)
        else:
            nexti = None

    # output
    return islands


if __name__ == '__main__':
    test = set()
    test.add((2, 2))
    test.add((2, 2))
    test.add((2, 2))
    test.add((2, 1))
    print(test)

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    grid3 = [
        ["1", "1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "0", "1"],
        ["1", "0", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1", "1"]
    ]

    # running test on grids and their manipulation
    # print(grid1.find("1"))

    out1 = numIslands(grid1)
    print("GRID #1")
    out2 = numIslands(grid2)
    print("GRID #2")
    out3 = numIslands(grid3)
    print("GRID #3")
    print(f'number of islands: {out1}')
    print(f'number of islands: {out2}')
    print(f'number of islands: {out3}')
