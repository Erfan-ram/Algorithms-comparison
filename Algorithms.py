def devide_conquer(number):
    if number < 2:
        return number

    else:
        return devide_conquer(number-1)+devide_conquer(number-2)


def dynamic_programming(number):
    f = [0, 1]

    for i in range(2, number+1):
        f.append(f[i-1] + f[i-2])
    return f[number]
