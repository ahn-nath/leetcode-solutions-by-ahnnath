# we will try to adapt it to the uneven version, but this should work for the even version
# NOTE: this does not work
def longestPalindrome(s: str) -> int:
    # check for base case: string is equal to 1 or is palindrome
    if reversed(s) == s or len(s) == 1:
        return len(s)

    char_counts = {}

    # get count of each char
    for c in s:
        if char_counts.get(c):
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    counts = list(char_counts.values())

    # evaluate the longest palindrome possible with greedy approach
    longest = len(s) - 1
    while longest > 1:
        # evaluate if even or uneven
        is_even = False
        if longest % 2 == 0:
            is_even = True

        # we start the evaluation
        # this denotes the number of counts that are equal or more than half the longest palindrome length
        equal_pair = 0
        half = longest // 2
        more_than_two = 0
        more_than_two_goal = longest / 2
        can_be_extra = False
        for count in counts:

            # case #1: if we have a char with count equal or more than then longest possible palindrome, return
            if count >= longest:
                return longest

            # case #special
            if count == 1 or count >= half:
                can_be_extra = True

            # case #2
            if count >= half:
                equal_pair += 1

                if equal_pair >= 2:
                    if is_even:
                        return longest
                    elif can_be_extra:
                        return longest
            # case #3
            if count >= 2:
                more_than_two += 1
                if more_than_two == more_than_two_goal:
                    if is_even:
                        return longest
                    elif can_be_extra:
                        return longest

        # after the evaluation we update the longest possible for the next iteration
        longest -= 1


def longestPalindrome(s: str) -> int:
    # check for base case: string is equal to 1 or is palindrome
    if reversed(s) == s or len(s) == 1:
        return len(s)

    char_counts = {}

    # get count of each char
    for c in s:
        if char_counts.get(c):
            char_counts[c] += 1
        else:
            char_counts[c] = 1

    counts = list(char_counts.values())
    evens, odds = 0, 0
    add_1 = False
    for count in counts:
        if count % 2 == 0:
            evens += count
        else:
            odds += count - 1
            add_1 = True

    longest = evens + odds
    if add_1:
        return longest + 1

    return longest


if __name__ == '__main__':
    # examples with even numbers
    print(longestPalindrome(s="a"))  # 1
    print(longestPalindrome(s="a11"))  # 2
    print(longestPalindrome(s="x1001"))  # 4
    print(longestPalindrome(s="x102201"))  # 6
    print(longestPalindrome(s="x10233201"))  # 8

    # actual test from Leetcode
    print(longestPalindrome(s="abccccdd"))  # 1
    print(longestPalindrome(s="a"))
