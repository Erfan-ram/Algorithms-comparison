def devide_conquer(number):
    if number < 2:
        return number

    else:
        return devide_conquer(number-1)+devide_conquer(number-2)
