from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    # you need to pass the position to use as a tuple (first)
    stack = [(0, 0)]

    # repeat with the next item in stack
    while stack:
        cell = stack.pop()
        cell_val = board[cell[0], cell[1]]

        # handle neighbors; define the horizontal, vertical and diagonal positions
        live_neighbors = 0
        dead_neighbors = 0

        # horizontal
        left = board(cell[0], cell[1] - 1) if cell[1] - 1 >= 0 else None
        right = board(cell[0], cell[1] + 1) if cell[1] + 1 < len(board[0]) else None

        # TODO: make the following logic a function that updates relevant variables
        if left == 1 or left == "l":
            live_neighbors += 1

            if left == 1:
                stack.append(())
                board[cell[0], cell[1] - 1] = "l"
        else:
            dead_neighbors += 1
            if left == 0:
                board[cell[0], cell[1] - 1] = "d"

        if right == 1 or right == "l":
            live_neighbors += 1

            if right == 1:
                stack.append(())
                board[cell[0], cell[1] + 1] = "l"
            else:
                dead_neighbors += 1
                if right == 0:
                    board[cell[0], cell[1] + 1] = "d"

        # vertical
        top = board(cell[0] - 1, cell[1]) if cell[0] - 1 >= 0 else None
        bottom = board(cell[0] + 1, cell[1]) if cell[0] + 1 < len(board) else None

        if top == 1 or top == "l":
            live_neighbors += 1

            if top == 1:
                stack.append(())
                board[cell[0] - 1, cell[1]] = "l"
        else:
            dead_neighbors += 1
            if top == 0:
                board[cell[0] - 1, cell[1]] = "d"

        if bottom == 1 or bottom == "l":
            live_neighbors += 1

            if bottom == 1:
                stack.append(())
                board[cell[0] + 1, cell[1]] = "l"
        else:
            dead_neighbors += 1
            if bottom == 0:
                board[cell[0] + 1, cell[1]] = "d"
        # diagonal
        # left group
        up_left = board[cell[0] - 1, cell[1] - 1] if cell[0] - 1 >= 0 and cell[1] - 1 >= 0 else None
        bottom_left = board[cell[0] + 1, cell[1] - 1] if cell[0] + 1 < len(board) and cell[1] - 1 >= 0 else None

        if up_left == 1 or up_left == "l":
            live_neighbors += 1

            if up_left == 1:
                stack.append(())
                board[cell[0] - 1, cell[1] - 1] = "l"
        else:
            dead_neighbors += 1
            if up_left == 0:
                board[cell[0] - 1, cell[1] - 1] = "d"

        if bottom_left == 1 or bottom_left == "l":
            live_neighbors += 1

            if bottom_left == 1:
                stack.append(())
                board[cell[0] + 1, cell[1] - 1] = "l"
        else:
            dead_neighbors += 1
            if bottom_left == 0:
                board[cell[0] + 1, cell[1] - 1] = "d"

        # right group
        up_right = board[cell[0] - 1, cell[1] + 1] if cell[0] - 1 >= 0 and cell[1] + 1 > len(board) else None
        bottom_right = board[cell[0] + 1, cell[1] + 1] if cell[0] + 1 < len(board) and cell[1] + 1 < len(
            board[0]) else None

        if up_right == 1 or up_right == "l":
            live_neighbors += 1

            if up_right == 1:
                stack.append(())
                board[cell[0] - 1, cell[1] + 1] = "l"
        else:
            dead_neighbors += 1
            if up_right == 0:
                board[cell[0] - 1, cell[1] + 1] = "d"

        if bottom_right == 1 or bottom_right == "l":
            live_neighbors += 1

            if bottom_right == 1:
                stack.append(())
                board[cell[0] + 1, cell[1] + 1] = "l"
        else:
            dead_neighbors += 1
            if bottom_right == 0:
                board[cell[0] + 1, cell[1] + 1] = "d"

        # check conditions and update with "l" or "d"
        # if current cell is live
        if cell_val == 1:
            # any live cell with fewer than two live neighbors dies as if caused by under-population
            if live_neighbors <= 2:
                cell_val = "d"
            # any live cell with more than three live neighbors dies, as if by over-population
            elif live_neighbors > 3:
                cell_val = "d"
            # any live cell with two or three live neighbors lives on to the next generation
            else:
                cell_val = "l"

        # if current cell is dead
        else:
            # any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            if live_neighbors == 3:
                cell_val = "l"
        # update cell val
        board[cell[0], cell[1]] = cell_val

        # after the stack is empty, replace "l" and "d" with 1 and 0
        elem = "d"
        if elem == "d":
            elem = 0
        else:
            elem = 1

            # return the matrix
        return board


# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
if __name__ == '__main__':
    gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
