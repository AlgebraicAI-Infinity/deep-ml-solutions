# Problem link : https://www.deep-ml.com/problems/2?from=Linear%20Algebra
# RESOURCE : https://en.wikipedia.org/wiki/Transpose
"""
    Time complexity : O(C*R)
    Space complexity : O(C*R)
    C --> columns of matrix
    r --> rows of matrix
"""

class Solution :
    @staticmethod
    def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
        if not a or not a[0]:
            return []
        
        rows=len(a)
        cols=len(a[0])
        transposed=[]

        for col in range(cols):
            transformation=[]
            for row in range(rows):
                transformation.append(a[row][col])
            transposed.append(transformation)
        return transposed
    
    """ Another way of doing this  """
    @staticmethod
    def trasnpose_of_matrix(a:list[list[int|float]]) -> list[list[int|float]]:
        row = len(nums)
        col=len(nums[0])
        transpose= [[0] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                transpose[i][j]=nums[j][i]

        return transpose


sol=Solution()
nums=[[1,2],[3,4]]
ans=sol.transpose_matrix(nums)
ans1 = sol.trasnpose_of_matrix(nums)
print(ans1)