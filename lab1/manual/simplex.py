def pivot(arr, arr_q, arr_basis):
    rel = []
    end = len(arr[1]) - 1
    min_el = 99999
    el = min(arr_q)
    index_row = 0
    index_column = 0
    current_el = 0
    current = 0

    for i in range(len(arr_q)):
        if el == arr_q[i]:
            index_column = i

    for i in range(len(arr)):
        if arr[i][index_column] != 0:
            current = arr[i][end] / arr[i][index_column]
            if current <= 0:
                rel.append(-1)
            elif current < min_el:
                min_el = current
                rel.append(current)
        else:
            rel.append(-1)

    for i in range(len(rel)):
        if min_el == rel[i]:
            index_row = i

    current_el = arr[index_row][index_column]

    for j in range(len(arr[index_row])):
        arr[index_row][j] = round(arr[index_row][j] / current_el, 3)

    for i in range(len(arr)):
        if i != index_row:
            el = arr[i][index_column]
            for j in range(len(arr[i])):
                k = arr[index_row][j] * el
                arr[i][j] = round(arr[i][j] - k, 3)

    arr_q_el = arr_q[index_column]
    for i in range(len(arr_q)):
        arr_q[i] = round(arr_q[i] - arr[index_row][i] * arr_q_el, 3)

    arr_basis.append(index_column)


def solve(arr, arr_q):
    init_obj = list(map(lambda x: x * (-1), arr_q))
    arr_basis = []
    res = []

    flag = True
    while flag:
        el = min(arr_q)
        if el >= 0:
            flag = False
        else:
            pivot(arr, arr_q, arr_basis)

    for i in range(len(arr)):
        for j in arr_basis:
            if arr[i][j] == 1:
                res.append((j + 1, arr[i][len(arr[i]) - 1]))

    obj = 0
    for var in res:
        obj = obj + init_obj[var[0] - 1] * var[1]

    return (obj, res)
