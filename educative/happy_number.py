def find_square_sum(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def happy_number(input_num):
    # Declare two pointers slow and fast
    slow = input_num
    fast = input_num

    # iterate through the sequence of numbers, slow moves one step at a time and fast moves two steps at a time
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck at 1
