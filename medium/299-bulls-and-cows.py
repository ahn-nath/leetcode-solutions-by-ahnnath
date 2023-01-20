def getHint(secret: str, guess: str) -> str:
    bulls_mapper = {}
    bulls, cows = 0, 0
    container = []

    # initialize mappers to know when we have a bull and when we have a cow
    for i, char in enumerate(secret):
        bulls_mapper[i] = char

    # check guess to track bulls and cows
    for i, char in enumerate(guess):
        # first check if it is a bull (right value at the right index)
        if bulls_mapper[i] == char:
            bulls += 1
            del bulls_mapper[i]

        else:
            container.append(char)

    values = list(bulls_mapper.values())
    for char in container:
        if char in values:
            cows += 1
            values.remove(char)


    # format final result
    return "{x}A{y}B".format(x=bulls, y=cows)


if __name__ == '__main__':
    getHint(secret="1807", guess="7810")  # "1A3B"
    getHint(secret="1123", guess="0111")  # "1A1B"
    getHint(secret="1122", guess="1222")

