# Problem Link : https://www.deep-ml.com/problems/76?from=Linear%20Algebra
# Resources : https://en.wikipedia.org/wiki/Cosine_similarity
# Contributor : Vivek Sharma

import math
import numpy as np
class Solution:
    @staticmethod
    def cosineSimilarity(vector1:list[float],vector2:list[float])->float:
        if len(vector1) != len(vector2):
            raise ValueError('The length of two vectors are not same')
        dot_product = sum(x*y for x,y in zip(vector1,vector2))
        magnitude_of_vector1 = math.sqrt(sum(x*x for x in vector1))
        magnitude_of_vector2 = math.sqrt(sum(y*y for y in vector2))
        if magnitude_of_vector1==0 or magnitude_of_vector2==0:
            return 0
        return dot_product/(magnitude_of_vector1*magnitude_of_vector2)
    
    """using Numpy"""
    @staticmethod
    def cosineSimilaityNp(vector1,vector2):
        x1 = np.array(vector1)
        x2 = np.array(vector2)
        dot_product = np.dot(x1,x2)
        magnitude = np.linalg.norm(x1)*np.linalg.norm(x2)
        return dot_product/magnitude

sol=Solution()
vector1 = [1,2,3]
vector2 = [4,5,6]
ans=sol.cosineSimilarity(vector1,vector2)
ans1 =sol.cosineSimilaityNp(vector1,vector2)
print(ans1)