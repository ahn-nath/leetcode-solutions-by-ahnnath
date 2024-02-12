def is_palindrome(s):
    # initialize pointers
    start = 0
    end = len(s) - 1

    # check whether or not the current pair of characters is identical
    if s[start] == s[end]:
        # keep iterating toward the middle until the meet
        while start != end:
            start += 1
            end -= 1

            if s[start] != s[end]:
                return False

        # if they reach the middle of the string without finding a mismatch, return 'True'
        return True

    return False


if __name__ == '__main__':
    # Output with chosen alternative
    print(is_palindrome(s='kayak'))  # True
    print(is_palindrome(s="racecar"))  # True
    print(is_palindrome(s="hello"))  # False
    print(is_palindrome(s="world"))  # False
    print(is_palindrome(s="madam"))  # True
    print(is_palindrome(s="nursesrun"))  # True
    print(is_palindrome(s="nurses run"))  # False
    print(is_palindrome(s="nurses run"))  # False
    print(is_palindrome(s="nursesrun"))  # True
