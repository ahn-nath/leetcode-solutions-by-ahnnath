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
    end = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # iterate over string and append every character, except for closing brackets ("]")
    for letter in s:
        if letter != "]":
            stack.append(letter)
        # if a closing bracket, we will resolve the string inside and multiply the resulting string by the digit
        else:
            l_internal = stack.pop()
            resulting_string = ""
            # pop everything until you reach a digit
            while l_internal not in digits:
                # if not an opening bracket, keep iterating and appending
                if l_internal != "[":
                    resulting_string = l_internal + resulting_string
                # pop next letter
                l_internal = stack.pop()
            # the resulting string to append next to be multiplied by the digit(s) followed by the opening bracket
            number = ''
            # while loop to track all digits in one string
            '''
            while l_internal in digits:
                number = l_internal + number
                if stack:
                    l_internal = stack.pop()
                else:
                    break
            '''
            item = l_internal
            while item in digits:
                number = item + number
                if stack and stack[-1] in digits:
                    item = stack.pop()
                else:
                    break

            # multiply the value by the resulting string
            resulting_string = resulting_string * int(number)
            stack.append(resulting_string)

    # output
    out = ''.join(map(str, stack))
    print("out for {} is: {}".format(s, out))
    return out


if __name__ == '__main__':
    """
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    
    """

    """
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    
    """

    decodeString(s="100[leetcode]")
    decodeString(s="2[abc]3[cd]ef")  # "abcabccdcdcdef"
    decodeString(s="3[a2[c]]")  # "accaccacc"
    decodeString(s="3[a]2[bc]")  # "aaabcbc"
