from typing import List


def findJudge1(n: int, trust: List[List[int]]) -> int:
    suspect = trust[0][1]
    for arr in trust:
        if arr[1] != suspect:
            print(-1)
            return -1

    print(suspect)
    return suspect


def findJudge(n: int, trust: List[List[int]]) -> int:
    if not trust and n == 1:
        return 1

    suspects = {}
    people = set()
    for arr in trust:
        suspect = arr[1]
        person = arr[0]
        if suspect in suspects:
            suspects[suspect] += 1
        else:
            suspects[suspect] = 1
        people.add(person)

    if people and suspects:
        max_key = max(suspects, key=suspects.get)
        if suspects[max_key] == n - 1 and max_key not in people:
            return max_key

    return -1


if __name__ == '__main__':
    findJudge(n=2, trust=[[1, 2]])
    findJudge(n=3, trust=[[1, 3], [2, 3]])
    findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]])
    findJudge(n=1, trust=[])
