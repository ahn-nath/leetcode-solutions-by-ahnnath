from typing import List


def largestAltitude(gain: List[int]) -> int:
    max_alt = 0
    suma = 0

    for ele in gain:
        suma += ele

        # if suma > max_atl, record
        if suma > max_alt:
            max_alt = suma

    print(max_alt)
    return max_alt


if __name__ == '__main__':
    largestAltitude(gain=[-5, 1, 5, 0, -7])  # 1
    largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2])  # 0
