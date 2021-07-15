import numpy as np
from eig_Tao import Tao_eigenvectors

A = np.array([[1,1,-1],[1,3,1],[-1,1,3]])

print(Tao_eigenvectors(A))