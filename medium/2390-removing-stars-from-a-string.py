def removeStars(s: str) -> str:
    stack = []

    # iterate over string
    for char in s:
        # if star, skip appending
        if char == "*":
            # remove closest to the left if possible
            if stack:
                stack.pop()
            continue
        # else, append char
        stack.append(char)

    # out
    return "".join(stack)


if __name__ == '__main__':
    removeStars(s="leet**cod*e")  # "lecoe"
    removeStars(s="erase*****")  # ""