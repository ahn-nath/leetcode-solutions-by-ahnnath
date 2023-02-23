from typing import List


def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
    # NOTE: an optimized version of this would be to perform the difference of each connected pair or their sum
    xor_result = []
    map_queries = {}
    # resolve the queries by iterating the queries arr
    for q in queries:
        str_q = str(q)
        # check if query already exist
        if str_q in map_queries:
            # append result
            xor_result.append(map_queries[str(q)])
        else:
            # if not, perform
            selection = arr[q[0]:q[1] + 1]

            suma = 0
            # accumulate the result of each bitwise operation
            for n in selection:
                suma ^= n
            # append the result and record
            xor_result.append(suma)
            map_queries[str_q] = suma

    print("result", xor_result)
    return xor_result


if __name__ == '__main__':
    xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]])  # Output: [2,7,14,8]
    xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]])  # Output: [8, 0, 4, 4]

    # test
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]

    '''
    sum = 0
    for n in arr:
        sum ^= n
        print(sum)

    print("another thing", arr[0] ^ arr[1])
    print("another thing", arr[1] ^ arr[2])
    '''
