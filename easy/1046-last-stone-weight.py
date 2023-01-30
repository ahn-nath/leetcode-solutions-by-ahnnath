from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    # while we have two stones to smash together, run
    while len(stones) > 1:
        # get the heaviest stone
        big = max(stones)
        first = stones.pop(stones.index(big))
        # get the second-heaviest stone
        big = max(stones)
        second = stones.pop(stones.index(big))

        # if they are not the same, deduct the second form the first and store result
        if first != second:
            new_stone = first - second
            stones.append(new_stone)

    # if we have any stones, return last
    if stones:
        return stones.pop()
    # else, return 0
    return 0


if __name__ == '__main__':
    lastStoneWeight(stones=[2, 7, 4, 1, 8, 1])
    lastStoneWeight(stones=[1])
    lastStoneWeight(stones=[2, 2])
