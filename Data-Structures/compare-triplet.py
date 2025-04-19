def compareTriplets(a, b):
    result = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            result[0] += 1
        elif b[i] > a[i]:
            result[1] += 1
        else:
            continue
    return result