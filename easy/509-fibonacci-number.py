def fib(n: int) -> int:
    # if n is zero, there are no iterations we need to make
    if n == 0:
        return 0

        # prev will always take the last's addend in future operations
    prev = 0
    # next will take the last value of 'res' or the result as a new addend
    nexti = 1

    # from 1 till n, sum
    for _ in range(0, n):
        res = prev + nexti
        prev = nexti
        nexti = res

    return res

if __name__ == '__main__':
    # examples
    print(fib(8))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(1))
