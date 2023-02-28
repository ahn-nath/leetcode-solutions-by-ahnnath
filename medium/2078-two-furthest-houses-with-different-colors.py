from typing import List


def maxDistance(colors: List[int]) -> int:
    # pointers
    l, r = 0, len(colors) - 1
    # initialize
    first_house = colors[l]
    second_house = colors[r]
    max_distance = 0
    # iterate over arr to find max distance
    while l < r < len(colors):
        if first_house == second_house:
            # shift the right pointer to evaluate the next farthest elem
            r = r - 1 if r - 1 >= 0 else -1
            # set second house
            second_house = colors[r]
        else:
            # record the distance if if greater that current max_distance
            distance = abs(r - l)
            if distance > max_distance:
                max_distance = distance

            # shift the left pointer to evaluate the next max distance
            l = l + 1 if l + 1 < len(colors) else len(colors) + 1
            r = len(colors) - 1

            # update houses
            first_house = colors[l]
            second_house = colors[r]

            """ 
            If the max_distance is greater than the difference between r and l, return max_distance
            The maximum distance possible by the next options will always be (len(colors) - 1) - (the current) l
            """
            if r - l < max_distance:
                return max_distance
    # out
    return max_distance


if __name__ == '__main__':
    maxDistance(colors=[1, 1, 1, 6, 1, 1, 1])  # 3
    maxDistance(colors=[0, 1])  # 1
    maxDistance(colors=[1, 8, 3, 8, 3])  # 4
    maxDistance(colors=[4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4])  # 8
