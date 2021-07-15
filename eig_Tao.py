import numpy as np
from scipy import linalg as lg


def product(lambda_i, lambdas_list):
    r = 1    
    for k in range(len(lambdas_list)):
        r = r*(lambda_i - lambdas_list[k])
    
    return r

def avoiding_product(lambda_i, lambdas_list,avoid):
    r = 1    
    for k in range(len(lambdas_list)):
        if k != avoid:
            r = r*(lambda_i - lambdas_list[k])
        else:
            continue
    return r


def new_method(A):
    eigenvectors = []
    
    eigenvalues = lg.eigh(A, eigvals_only=True)
    n_eigvs = len(eigenvalues)
    
    for i in range(n_eigvs):
        
        eigenvector_i = []
        lambda_i = eigenvalues[i]
        eigenvalues_product = avoiding_product(lambda_i,eigenvalues,i)
    
        for j in range(n_eigvs):

            M_j = np.delete(np.delete(A,j,axis=0), j, axis=1)
            eigenvalues_M_j = lg.eigh(M_j,eigvals_only=True)

            minor_product = product(lambda_i,eigenvalues_M_j)
            eigenvector_i.append(minor_product/eigenvalues_product)

        eigenvectors.append(eigenvector_i)
    
    return np.sqrt(np.array(eigenvectors, dtype=np.float16))