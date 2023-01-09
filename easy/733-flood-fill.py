from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    # get the initial color other adjacent pixels should be
    initial_color = image[sr][sc]
    stack = [(sr, sc)]

    # if the initial color is the same as the color we want to change to, return the image
    if initial_color == color:
        return image

    # while stack has something to look for
    while len(stack) != 0:
        # set current to latest element
        current = stack.pop()
        sr, sc = current

        # check if current is target, to stop search
        if image[sr][sc] == initial_color:
            image[sr][sc] = color

            # handle children
            # left = (sr, sc - 1) if sc - 1 >= 0 else None
            left = image[sr][sc - 1] if sc - 1 >= 0 else None
            # right = (sr, sc + 1) if sc + 1 < len(image[0]) else None
            right = image[sr][sc + 1] if sc + 1 < len(image[sr]) else None
            # top = (sr - 1, sc) if sr - 1 >= 0 else None
            top = image[sr - 1][sc] if sr - 1 >= 0 else None
            # bottom = (sr + 1, sc) if sr + 1 < len(image) else None
            bottom = image[sr + 1][sc] if sr + 1 < len(image) else None

            # check if adjacent pixels are present (top, bottom, left, right)
            if top == initial_color:
                stack.append((sr - 1, sc))

            if bottom == initial_color:
                stack.append((sr + 1, sc))

            if left == initial_color:
                stack.append((sr, sc - 1))

            if right == initial_color:
                stack.append((sr, sc + 1))

    # output
    return image


if __name__ == '__main__':
    # examples
    out1 = floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    out2 = floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0)

    # print output
    print(out1)
    print(out2)
