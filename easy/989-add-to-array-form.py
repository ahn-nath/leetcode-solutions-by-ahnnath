from typing import List


def addToArrayForm(num: List[int], k: int) -> List[int]:
    s = ''
    # iterate over each item and append to string
    for n in num:
        s += str(n)
    # sum k and s
    result = k + int(s)
    # convert result to list/array
    array_form = []
    for n in str(result):
        n = int(n)
        array_form.append(n)

    # out
    print(array_form)
    return array_form


if __name__ == '__main__':
    addToArrayForm(num=[1, 2, 0, 0], k=34)  # [1,2,3,4]
    addToArrayForm(num=[2, 7, 4], k=181)  # [4,5,5]
    addToArrayForm(num=[2, 1, 5], k=806)  # [1,0,2,1]
