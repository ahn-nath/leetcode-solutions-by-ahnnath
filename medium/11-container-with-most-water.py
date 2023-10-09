from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0
    max_height = max(height)

    front = 0
    back = len(height) - 1
    distance = len(height)

    while front < len(height) - 1 and back > 0:
        cur_height = min(height[front], height[back])
        distance -= 1
        area = cur_height * distance

        if area > max_area:
            max_area = area

        # check if it is possible to get a max_area greater than the current
        if max_area >= (max_height * (distance - 1)):
            print(max_area)
            return max_area

        if height[front] < height[back]:
            front += 1
        else:
            back -= 1
        # NOTE: consider checking if this values may reach the very limit and cause an out of bonds exception

    return max_area


if __name__ == '__main__':
    '''
    maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])  # 49
    maxArea(height=[1, 1])4
    '''
    maxArea(height=[2, 3, 10, 5, 7, 8, 9]) # 36 should be the output
