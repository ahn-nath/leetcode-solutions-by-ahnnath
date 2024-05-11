from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    # get total size of elements
    total = len(grid) * 2
    # get initial elements from grid (rows)
    strings_grid = {"-".join(str(e) for e in arr) for arr in grid}

    # get left elements from grid (columns)
    for i in range(len(grid)):
        # give the ith element for each arr in list
        col_val = [ele[i] for ele in grid]
        str_col = "-".join(str(e) for e in col_val)
        strings_grid.add(str_col)

    if len(strings_grid) == 1:
        print(total)
        return total

    print("all", strings_grid)

    out = total - len(strings_grid)

    print(out)
    return out


def equalPairs(grid: List[List[int]]) -> int:
    # track pairs with a dictionary
    pairs_ver = {}
    pairs_hor = {}

    # track horizontally
    for j in range(len(grid)):
        hor_ele = ''
        for i in range(len(grid)):
            hor_ele += str(grid[j][i])

            if i < len(grid) - 1:
                hor_ele += '-'

        # here dictionary check
        print(hor_ele)
        if hor_ele in pairs_ver:
            pairs_ver[hor_ele] += 1
        else:
            pairs_ver[hor_ele] = 1

    # track vertically
    for j in range(len(grid)):
        ver_ele = ''
        for i in range(len(grid)):
            ver_ele += str(grid[i][j])

            if i < len(grid) - 1:
                ver_ele += '-'

        # here dictionary check
        print("ver:", ver_ele)
        if ver_ele in pairs_hor:
            pairs_hor[ver_ele] += 1
        else:
            pairs_hor[ver_ele] = 1

    c = 0
    for key in pairs_ver:
        if key in pairs_hor:
            c += pairs_hor[key] * pairs_ver[key]
            print(pairs_hor)
            print(pairs_ver)

    print(c)


if __name__ == '__main__':
    equalPairs(grid=
               [[3, 3, 3, 6, 18, 3, 3, 3, 3, 3], [3, 3, 3, 3, 1, 3, 3, 3, 3, 3], [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 1, 3, 3, 3, 3, 3], [1, 1, 1, 11, 19, 1, 1, 1, 1, 1],
                [3, 3, 3, 18, 19, 3, 3, 3, 3, 3], [3, 3, 3, 3, 1, 3, 3, 3, 3, 3], [3, 3, 3, 3, 1, 3, 3, 3, 3, 3],
                [3, 3, 3, 1, 6, 3, 3, 3, 3, 3], [3, 3, 3, 3, 1, 3, 3, 3, 3, 3]])
    # equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]])  # 1
    # equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])  # 3
    # equalPairs([[11, 1], [1, 11]])  # 2 (?)
    # equalPairs([[13, 13], [13, 13]])  # 4
