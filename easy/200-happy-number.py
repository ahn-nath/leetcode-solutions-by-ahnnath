def isHappy(n: int) -> bool:
    print("\ncandidate:", n)

    previous_calculations = []
    single_digits = [1, 2, 3, 4, 5, 6, 8, 9]

    # if the number is a single digit
    if n in single_digits:
        return False

    # if the number can be divided by 10
    if n % 10 == 0 and str(n)[0] != '1':
        return False

    suma = n
    number = n
    while suma not in previous_calculations:
        previous_calculations.append(suma)
        number = suma
        suma = 0
        for d in str(number):
            suma += int(d) ** 2

        print("final suma:", suma)
        if suma == 1:
            return True


        # if the number is a single digit
        if  n in single_digits:
            return False

            # if the number can be divided by 10
        if suma % 10 == 0 and str(suma)[0] != '1':
            return False


    return False


# if the number already exist in arr


if __name__ == '__main__':
    print(isHappy(19))
    print(isHappy(2))
    print(isHappy(21))
    print(isHappy(7))
