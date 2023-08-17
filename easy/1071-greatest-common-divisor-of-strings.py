# NOTE: 33 cases passed
def gcdOfStrings_a2(str1: str, str2: str) -> str:
    # we define the roles
    print(len(str1))
    print(len(str2))

    if len(str1) > len(str2):
        longest = str1
        shortest = str2
    else:
        longest = str2
        shortest = str1

    # we get the length of the string we find the separator
    length_traversed = len(shortest)
    # iterate over the short string to find the longest possible separator, if existent
    while length_traversed > 1:
        # we get the slice of 'shortest'
        sliced = shortest[:length_traversed]
        # we split the longest string to find if it divides it
        split_string = longest.split(sliced)
        split_len = len(split_string) - 1

        # if it divides it, the total number of characters values should be equal to the longest string lenght
        if split_len * length_traversed == len(longest):
            print(sliced)
            return sliced

        # if no separator found, continue with the next longest separator
        length_traversed -= 1

    # if no separator found, return empty string
    print("nothing")
    return ""


# NOTE: 33 cases passed
def gcdOfStrings_a2(str1: str, str2: str) -> str:
    # we define the roles
    if len(str1) > len(str2):
        longest = str1
        shortest = str2
    else:
        longest = str2
        shortest = str1

    length_traversed = len(shortest)
    length_longest = len(longest)

    # iterate over the shortest string to find the longest possible separator, if existent
    while length_traversed > 1:
        # slice the shortest string and capture the len
        sliced = shortest[:length_traversed]
        sliced_len = len(sliced)
        i, difference = 0, 0

        # while we have not reached the end of the longest, compare substrings with potential separator
        while i < length_longest:
            # advance the sliced len over the string and check if each piece is the same,
            longest_slice = longest[i:i + sliced_len]
            # if so, sum the difference
            if longest_slice == sliced:
                difference += sliced_len

            # if not, break the loop to find for the next possible separator
            else:
                break

            # record number of indexed already traversed
            i += sliced_len

        # after each separator check, compare results to see if any difference matches the longest string length
        if difference == length_longest:
            print(sliced)
            return sliced
        # move forward with the next potential longest separator
        length_traversed -= 1

    # if no separator found, return empty string
    print("nothing")
    return ""


# NOTE: 73/123 passed
def gcdOfStrings(str1: str, str2: str) -> str:
    # define roles
    if len(str1) > len(str2):
        largest = str1
        smallest = str2
    else:
        largest = str2
        smallest = str1

    # r1: both strings must have the same (unique) characters
    if set(str1) != set(str2):
        return ""

    # find all possible candidates for the divisor
    # len, starting from the back, with reverse step
    for i in range(len(smallest), 0, -1):
        # slice the string
        sliced = smallest[:i]

        # r2: the slice length must divide the string length evenly
        if len(smallest) % len(sliced) != 0 or len(largest) % len(sliced) != 0:
            continue

        # r3: the slice (sliced) will be multiplied to match the strings
        divisor_1 = len(largest) // len(sliced)
        divisor_2 = len(smallest) // len(sliced)

        result_1 = sliced * divisor_1
        result_2 = sliced * divisor_2

        # if the result of multiplying the string by the needed parts to complete the largest and
        # smallest string, continue with the next slide
        if result_1 == largest and result_2 == smallest:
            return sliced

    # no divisor found
    return ""


if __name__ == '__main__':

    str1 = "ABCABCABC"
    str2 = "ABC"

    str3 = "ABABAB"
    str4 = "ABAB"

    str5 = "LEET"
    str6 = "CODE"

    str7 = "ABABABAB"
    str8 = "ABAB"

    str1 = "ABCABCABC"
    str2 = "ABCAAA"

    print(gcdOfStrings(str1, str2))  # ABC
    print(gcdOfStrings(str3, str4))  # AB
    print(gcdOfStrings(str5, str6))  # ""
    print(gcdOfStrings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX", str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))  # TAUXX
    print(gcdOfStrings(str7, str8))  # "ABAB"

    """
    # gcdOfStrings(str1, str2)
    # gcdOfStrings(str3, str4)
    # gcdOfStrings(str5, str6)
    gcdOfStrings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX", str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")

    # gcdOfStrings2(str1, str2)
    # gcdOfStrings2(str3, str4)
    # gcdOfStrings2(str5, str6)
    gcdOfStrings2(str1="TAUXXTAUXXTAUXXTAUXXTAUXX", str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
    """
