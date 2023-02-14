def decodeString(s: str) -> str:
    """
        This code decodes a string in accordance to a specific system for it. It takes the string and appends
        all characters until it reaches a closing bracket "]." When it does so, it starts popping or appending all
         characters before finding a closing bracket and digit and appends the resulting string to the stack to
         continue appending characters.

        :param s:
        :return: string
    """
    stack = []
    digits = []
    # iterate over string and append every character, except for closing brackets ("]")
    for letter in s:
        if not "]":
            stack.append(letter)
        # if a closing bracket, we will resolve the string inside and multiply the resulting string by the digit
        else:
            print(letter)
            l_internal = stack.pop()
            resulting_string = []
            # pop everything until you reach a digit
            while l_internal not in digits:
                # if not an opening bracket, keep iterating and appending
                if l_internal != "[":
                    resulting_string.append(l_internal)
                # pop next letter
                l_internal = stack.pop()
            # the resulting string to append next to be multiplied by the digit followed by the opening bracket
            resulting_string = resulting_string * l_internal
            stack.append(resulting_string)


if __name__ == '__main__':
    """
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    
    """

    """
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    
    """
    s = "abc" * 3
    print(s)
