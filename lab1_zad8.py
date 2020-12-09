import numpy as np


def matrix_mult_4b(A, B):
    m = A.shape[0]
    k = A.shape[1]
    n = B.shape[1]

    C = np.zeros((m, n))

    for j in range(n):
        C[0:m, j] = MatrixVext(A, B[0:k, j])  #np.dot(A, B[0:k, j])

    return C


def MatrixVext(A, B):
    C = np.zeros(A.shape[0])

    m = A.shape[0]

    for p in range(A.shape[1]):
        C += MultAndAdd(A[0:m, p], B[p])

    return C


def MultAndAdd(A, B):
    C = np.zeros(A.shape[0])

    for i in range(A.shape[0]):
        C[i] = A[i] * B

    return C


A = np.array([[1, 0, 2],
              [-1, 3,1],
              [0, 0, 1]])

B = np.array([[3, 1, 0],
              [2, 1, 0],
              [1, 0, 1]])

print(matrix_mult_4b(A, B))
