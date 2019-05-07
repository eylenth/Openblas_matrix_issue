import numpy as np

np.__config__.show()

matrix = np.loadtxt('data.txt')

n1 = np.dot(matrix, matrix)
n2 = np.dot(matrix, matrix)

print(np.array_equal(n1, n2))

np.testing.assert_array_equal(n1, n2)
