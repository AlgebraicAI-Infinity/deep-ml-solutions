# Problem Link : https://www.deep-ml.com/problems/35?from=Linear%20Algebra
# Resource : https://en.wikipedia.org/wiki/Diagonal_matrix
# Contributor : Vivek Sharma


import numpy as np

class Solution :
    """ proper numpy method """
    @staticmethod
    def vector_to_diagoal_matrix(vector:list[int]):
        diagonal_matrix = np.diag(vector)
        return diagonal_matrix
        
    """ Implementation from sratch"""
    @staticmethod
    def vector_to_diagonal_matrix_scratch_implementation(vector1) -> np.ndarray:
        vector1 = np.array(vector1)  
        n = len(vector1)
        diagonal_matrix = np.zeros((n, n), dtype=vector1.dtype)

        for i in range(n):
            diagonal_matrix[i][i] = vector1[i]

        return diagonal_matrix








sol=Solution()
nums=[1,2,3]
ans=sol.vector_to_diagoal_matrix(nums)
ans1 = sol.vector_to_diagonal_matrix_scratch_implementation(nums)
print(ans1)