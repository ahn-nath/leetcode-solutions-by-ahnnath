from typing import List


def sampleStats(count: List[int]) -> List[float]:
    count_dict = {}
    sample = []
    # generate the actual sample
    for i, val in enumerate(count):
        if val != 0:
            # track occurrences in dict to get the mode
            count_dict[i] = val
            # fill sample
            sample.extend(val * [i])

    # TODO: normalize the sample below with a float version
    # size
    size = len(sample)
    # min
    mini = min(sample)
    # max
    maxi = max(sample)
    # mean
    mean = sum(sample) / size
    # median
    # if we have an even
    if size % 2 == 0:
        half = (size // 2) - 1
        median = (sample[half] + sample[half + 1]) / 2
    else:
        middle = (size // 2) + 1
        median = sample[middle]

    # mode or most common number
    mode = max(count_dict, key=count_dict.get)

    # out
    print([mini, maxi, mean, median, mode])
    return [mini, maxi, mean, median, mode]


def get_value_in_position(count_dictionary, position_to_search):
    current_sum = 0
    for key, val in count_dictionary.items():
        current_sum += val
        if current_sum >= position_to_search:
            print(key)
            return key


# optimized way of calculating this answer:
def sampleStats(count: List[int]) -> List[float]:
    count_dict = {}
    sample = []
    # generate the actual sample
    for i, val in enumerate(count):
        if val != 0:
            # track occurrences in dict to get the mode
            count_dict[i] = val
            # fill sample
            sample.append(val * i)

    # TODO: normalize the sample below with a float version
    # size
    size = sum(count_dict.values())
    # min
    mini = min(count_dict)
    # max
    maxi = max(count_dict)
    # mean
    mean = sum(sample) / size
    # median
    median = None
    val = list(count_dict.values())

    if size % 2 == 0:
        base = (size // 2)
        middle_1 = get_value_in_position(count_dict, base)
        middle_2 = get_value_in_position(count_dict, base + 1)
        median = (middle_1 + middle_2) / 2
    else:
        base = (size // 2) + 1
        middle = get_value_in_position(count_dict, base)
        median = middle

    # mode or most common number
    mode = max(count_dict, key=count_dict.get)

    # out
    print([mini, maxi, mean, median, mode])
    return [mini, maxi, mean, median, mode]


if __name__ == '__main__':
    sampleStats(
        count=[0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
    sampleStats(
        count=[0, 4, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
