def sort_colors(colors):
    # Declare three pointers white, red and blue
    white = 0
    red = 0
    blue = len(colors) - 1

    # iterate through colors, moving elements to their correct positions based on their values
    while white <= blue:

        # we swap the values of both (white, red) in the array and increment both pointers by 1
        if colors[white] == 0:
            if colors[red] != 0:
                colors[white], colors[red] = colors[red], colors[white]
            white += 1
            red += 1

            # the number is in the correct position, so we just increment pointers by 1
        elif colors[white] == 1:
            white += 1

        # otherwise, we swap values of both (white, blue) in the array and increment both pointers by 1
        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1

    return colors


if __name__ == '__main__':
    # Output with chosen alternative
    print(sort_colors(colors=[0, 1, 0]))  # [0, 0, 1]
