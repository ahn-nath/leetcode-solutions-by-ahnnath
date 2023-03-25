# Number of Islands

# Intuition
Initially, I imagine that we did not need to count the islands, but just check the status of each cell and the connection that they have with other cells. 

Nevertheless, this was hard to accomplish. In a short explanation, because, in order to track pone islands, we need to continue looking or going through their connected cells, which could go up until the last row. But because more cells from another island or group could be untracked and because within the same island, it is easy to recheck the same cell several times due to it being connected to several cells, it was better to mark it. 

From the beginning, I figured we should start with the first cell, and continue looking for “water” or the end of the adjacent cells to count one island. 

# Approach
We start with the first cell and check if the value is “1” (equivalent to land). 
If the “current cell” is “0”, we check the next cell. Else, we will start a loop with it that will continue looking for connected/adjacent cells that are to its right, or left (horizontally connected) or to its top or bottom (vertically connected) and have a value equal to “1”. When the condition is met, we act them to a stack for future checks. We repeat the same process with each cell on the stack until there is nothing to check. Then, we get out of the loop and record “1” island, or in other words, add 1 to the counter. 
 
# Complexity
- Time complexity:
[to be added]

- Space complexity:
[to be added]

# Code
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
```
