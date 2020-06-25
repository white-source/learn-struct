import numpy as np

from scipy import linalg


a = np.array([[1,2], [3, 4]])
b = np.array([[-1, 0], [1, -2]])

c = a * b

d = a - b

e = 3 * a

from scipy import linalg
f = linalg.inv(a)
print(f)





A = np.array([[1, 2], [3, 4]])
la, v = linalg.eig(A)
print("the eigenvalues is: ", la)
print("the eigenvectors is: ", v)




A = np.array([[1,2,3],[-1,-2,-3]])
m, n = A.shape
U,s,Vh = linalg.svd(A)
Sig = linalg.diagsvd(s,m,n)


print("Matrix U: ", U)
print("Matrix Sigma: ", Sig)
print("Matrix Vt: ", Vh)
