def guess(number, pick):
    if pick > number:
        return 1
    if pick < number:
        return -1
    else:
        return 0


def guessNumber(n: int, pick) -> int:
    start = 1
    end = n

    while start <= end:
        middle = (start + end) // 2

        if guess(middle, pick) == 1:
            start = middle + 1

        elif guess(middle, pick) == -1:
            end = middle - 1
        else:
            return middle


if __name__ == '__main__':
    # examples
    print(guessNumber(n=2, pick=2))
    print(guessNumber(n=10, pick=6))
    print(guessNumber(n=1, pick=1))
    print(guessNumber(n=2, pick=1))

