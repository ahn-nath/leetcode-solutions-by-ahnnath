# Intuition


# Approach
<!-- Describe your approach to solving the problem. -->
    
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
def stringCleansing(original_s: str):
    """ This function will be used to remove the backspace characters from the string and get a resulting string
    without it that meets the conditions indicated by the present backspace characters """
    # used to track how many future characters to ignore in an iteration
    ignore_debt = 0
    # used to store the resulting string
    string_out = []

    # loop for the final output of s
    while original_s:
        curr_char = original_s.pop()
        # check if there is backspace character present
        if curr_char == "#":
            ignore_debt += 1
        # check if the present character should not be ignored
        elif ignore_debt > 0:
            ignore_debt -= 1
        # if none, add character to list
        else:
            string_out.insert(0, curr_char)

    return string_out


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # turn s and t into stacks/lists
        s = list(s)
        t = list(t)

        # we clean and get the resulting strings from both s and t
        t_out = stringCleansing(s)
        s_out = stringCleansing(t)

        # we compare the final result of both
        if t_out == s_out:
            return True

        return False
```