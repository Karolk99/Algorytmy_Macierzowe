import numpy as np


def col_gauss(A):
    n = A.shape[0]

    for k in range(n):
        A[k+1:n, k] = A[k+1:n, k] / A[k, k]
        for j in range(k+1, n):
            A[k+1:n, j] -= A[k+1:n, k] * A[k, j]

    return A


def gauss_with_pivoting(A, u=0.1):
    n = A.shape[0]

    for k in range(n):
        m = max([abs(x) for x in A[k:n, k]])
        m = u * m
        j_m = k
        for j in range(k, n):
            if abs(A[j, k]) >= m:
                j_m = j

        if abs(A[j_m, k]) == 0:
            raise Exception('macierz osobliwa')
        temp = np.zeros(n - k)
        if j_m != k:
            temp = np.array(A[k, k:n], copy=True)
            A[k, k:n] = np.array(A[j_m, k:n], copy=True)
            A[j_m, k:n] = np.array(temp, copy=True)

        A[k:n, k] = A[k:n, k] / A[k, k] #k+1 == u
        for j in range(k + 1, n):
            A[k:n, j] -= (A[k:n, k] * A[k, j]) #k+1 == u

    return A


A = np.array([[0., 4., 1.], [1., 1., 3.], [2., -2., 1.]])
print(A, end='\n\n')
# A = col_gauss(A)
# print(A)
A = gauss_with_pivoting(A)
print(A)


# def row_gauss(A):
#     n = A.shape[0]
#
#     for k in range(n):
#         akk = A[k, k]
#         A[k, k:n] = A[k, k:n] / akk
#         for j in range(k + 1, n):
#             A[j, k+1:n] = A[k, k+1:n] * A[j, k]
#
#     return A
#
#
# def gauss(A):
#     n = A.shape[1]
#
#     for k in range(1, n-1):
#         akk = A[k, k]
#         for j in range(k+1, n):
#             A[j, k:n] -= A[k, k:n] * A[j, k] / akk
#
#     return A
#
#
# A = np.array([[1., 1., 2.],
#               [1., 3., 1.],
#               [3., 2., 5.]])
#
# #print(gauss(A))
# print(col_gauss(A), '\n')

