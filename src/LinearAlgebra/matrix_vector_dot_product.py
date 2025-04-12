# Problem link : https://www.deep-ml.com/problems/1
""" Time complexity : O(m*n)
    Space complexity : O(n)
"""

class Solution :
    @staticmethod
    def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
        if not a or len(a[0]) != len(b):
            return -1

        result=[]
        for row in a :
            product=0
            for i in range(len(b)):
                product+=row[i]*b[i]
            result.append(product)
        return result	

sol=Solution()
a = [[1,2],[2,3]]
b = [3,4]
ans=sol.matrix_dot_vector(a,b)
print(ans)