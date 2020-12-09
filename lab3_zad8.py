import numpy as np


def element_to_csr(nelt, nvar, nval, columns, row_index, values):
    array = np.zeros((nvar, nvar))
    current_row = -1
    iterator = 0
    for i in range(nelt):
        while row_index[iterator] == i:
            current_row += 1
            iterator += 1
        add_to_matrix(array, values[i*4:i*4+4], current_row, columns[i])

    csr_values = []
    icl = []
    colptr = []

    current_row = -1
    for i in range(nvar):
        for j in range(nvar):
            if array[i, j] != 0:
                csr_values.append(array[i, j])
                icl.append(j)

                while current_row != i:
                    current_row += 1
                    colptr.append(len(icl) - 1)

    colptr.append(len(icl))

    return icl, colptr, csr_values


def add_to_matrix(array, values, row, col):
    array[row:row+2, col:col+2] += np.array([values[0:2],
                                            values[2:4]])


nelt = 2
nvar = 3
nval = 8
columns = [0, 1]
row_index = [0, 1, 2]
values = [1, 0, 0, 1, 1, 3, 0, 5]

icl, colptr, csr_values = element_to_csr(nelt, nvar, nval, columns, row_index, values)

print(icl)
print(colptr)
print(csr_values)