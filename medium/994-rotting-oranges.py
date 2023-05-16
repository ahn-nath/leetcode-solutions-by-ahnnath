from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    """
     This function takes in a grid of 0s, 1s, and 2s. 0s are empty cells, 1s are fresh oranges, and 2s are rotten oranges.
        The function returns the number of minutes it takes for all oranges to rot. If it is impossible for all oranges to rot, the function returns -1.

        @param grid: a grid of 0s, 1s, and 2s
        @return: the number of minutes it takes for all oranges to rot

    """
    minutes_count = 0
    # initialize with the first element in grid
    current_rotten_oranges_stack = []
    next_rotten_oranges_stack = []

    healthy_oranges_count = 0

    # initialize healthy_oranges_count and current_rotten_oranges_stack
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # count the number os healthy oranges
            if 1 == grid[row][column]:
                healthy_oranges_count += 1
            # track current rotten oranges
            if 2 == grid[row][column]:
                current_rotten_oranges_stack.append((row, column))

    # if there are no healthy oranges, return 0, because no minutes are needed
    if 0 == healthy_oranges_count:
        return 0

    # while there are healthy oranges and there are rotten oranges
    while current_rotten_oranges_stack and healthy_oranges_count > 0:
        # get current element
        ele = current_rotten_oranges_stack.pop()
        row = ele[0]
        column = ele[1]

        # check the top
        top = grid[row - 1][column] if row > 0 else 0
        # check the bottom
        bottom = grid[row + 1][column] if row < (len(grid) - 1) else 0
        # check the left
        left = grid[row][column - 1] if column > 0 else 0
        # check the right
        right = grid[row][column + 1] if column < (len(grid[0]) - 1) else 0

        # if any of the adjacent cells are healthy, rot them and add to oranges_stack, to see future oranges to rot
        if top == 1 or bottom == 1 or left == 1 or right == 1:

            if top == 1:
                # mark top as rotten
                grid[row - 1][column] = 2
                healthy_oranges_count -= 1
                # add to next_rotten_oranges_stack
                next_rotten_oranges_stack.append((row - 1, column))

            if bottom == 1:
                # mark bottom as rotten
                grid[row + 1][column] = 2
                healthy_oranges_count -= 1
                # add to next_rotten_oranges_stack
                next_rotten_oranges_stack.append((row + 1, column))

            if left == 1:
                # mark left as rotten
                grid[row][column - 1] = 2
                healthy_oranges_count -= 1
                # add to next_rotten_oranges_stack
                next_rotten_oranges_stack.append((row, column - 1))

            if right == 1:
                # mark right as rotten
                grid[row][column + 1] = 2
                healthy_oranges_count -= 1
                # add to next_rotten_oranges_stack
                next_rotten_oranges_stack.append((row, column + 1))

        # if we have reached the goal, set current rotten oranges as empty
        if healthy_oranges_count <= 0:
            current_rotten_oranges_stack = []

        # if pair_index is greater than the length of oranges_stack, reset it to 0 if there are still healthy oranges
        if len(current_rotten_oranges_stack) <= 0:
            # increment count
            minutes_count += 1
            # set current to next
            current_rotten_oranges_stack = next_rotten_oranges_stack
            next_rotten_oranges_stack = []

    # if there are still healthy oranges, return -1
    if healthy_oranges_count > 0:
        return -1

    # out
    return minutes_count


if __name__ == '__main__':
    orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]])  # 4

    orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]])  # -1

    orangesRotting(grid=
                   [[2, 1, 1], [1, 1, 1], [0, 1, 2]])  # 2

    orangesRotting(grid=[[0, 2]])  # 0

    orangesRotting(grid=[[1], [2]])  # 1

    orangesRotting(grid=
                   [[2, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])  # 58

    orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]])  # 2

    orangesRotting(grid=[[1, 1, 2, 0, 2, 0]])  # 2
