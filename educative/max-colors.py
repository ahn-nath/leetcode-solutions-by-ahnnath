def getMaxColors(prices, money):
    # our initial strategy will be to use a sliding window
    left = 0
    right = 0
    sum_price = prices[0]
    curr_window_size = 1
    max_window_size = 0

    # consider the base case of having just one item?? (test) # TODO: remove this after checking

    while left <= right < len(prices) - 1:

        # we keep sliding to the right and expanding our window as long as sum_price is not > money
        if sum_price < money or left == right:
            right += 1
            sum_price += prices[right]
            curr_window_size = curr_window_size + 1  # if sum_price <= money else curr_window_size

        # once it is, we will remove from the left until we return to an ideal balance
        else:
            sum_price -= prices[left]
            left += 1
            curr_window_size -= 1

        # we will keep a tracker that will be updated once we have a bigger number to compete
        if curr_window_size > max_window_size and (sum_price < money):
            max_window_size = curr_window_size

    print(max_window_size)
    return max_window_size


if __name__ == '__main__':
    getMaxColors([2, 3, 5, 1, 1, 2, 1], 7)  # 4
    getMaxColors([1, 2, 3, 4, 5], 10)  # 3
    getMaxColors([1, 2, 3, 4, 5], 3)  # 1
    getMaxColors([6, 1, 3, 1, 2, 5, 2], 4)  # 2
