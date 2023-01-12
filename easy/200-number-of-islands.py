from typing import List


def numIslands(grid: List[List[str]]) -> int:
    # if not empty
    if not grid:
        return 0

    islands = 0
    nexti = (0, 0)
    limit = len(grid)
    while nexti:
        er, ec = next
        # check if current cell is a land
        if grid[er][ec] == 1:
            # iterate over array to check for position having a land (1)
            stack = set(next)
            while stack:
                curr = stack.pop()
                sr, sc = curr

                # mark as 2
                grid[sr, sc] = 2
                # handle children
                left = grid[sr][sc - 1] if sc - 1 >= 0 else None
                right = grid[sr][sc + 1] if sc + 1 < len(grid[sr]) else None
                top = grid[sr - 1][sc] if sr - 1 >= 0 else None
                bottom = grid[sr + 1][sc] if sr + 1 < len(grid) else None

                # check if adjacent pixels are present (top, bottom, left, right)
                if top == 1:
                    stack.add((sr - 1, sc))
                if bottom == 1:
                    stack.add((sr + 1, sc))
                if left == 1:
                    stack.add((sr, sc - 1))
                if right == 1:
                    stack.add((sr, sc + 1))
            # when we get to the second loop, redefine er and ec
            # TODO: add the next number (column) because we know is likely empty, else next row
            ec = sc + 1 if sc+1 <  len(grid) else 0 # else first column
            er = er+1 if ec == 0 else er # else keep it simple because it is the same row but different column

                # redefine ec or er if necessary (not last items for example)
            # count island
            islands += 1
        # define next node/cell
        # check cell in the next column, if not last column
        if ec + 1 < limit:
            nexti = (er, ec + 1)
        # check first cell in the next row, if not last row
        elif er + 1 < limit:
            nexti = (er + 1, 0)
        else:
            nexti = None


if __name__ == '__main__':

    test = set()
    test.add((2,2))
    test.add((2, 2))
    test.add((2, 2))
    test.add((2, 1))
    print(test)
