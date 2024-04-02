def is_bad_version(v,
                   range_version):  # is_bad_version() is the API function that returns true or false depending upon whether the
    # provided version ID is bad or not
    return v >= range_version


# -----------------------------------------------

def first_bad_version(n, range_version):
    first = 1
    last = n
    middle = (first + last) // 2
    api_calls = 0

    while first <= last:
        if is_bad_version(middle, range_version):
            last = middle - 1
        else:
            first = middle + 1

        middle = (first + last) // 2
        api_calls += 1

    return [first, api_calls]


if __name__ == '__main__':
    # first_bad_version(5)  # 4
    first_bad_version(8, 6)
