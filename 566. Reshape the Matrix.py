'''
Tag: Array Difficulty: Easy

In MATLAB, there is a very useful function called 'reshape', 
which can reshape a matrix into a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, 
and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, 
output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. 
The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''

'''
For this question, 
using list1[] + list2[] = list3[] gives you all items in one list instead of a list in a list like list.append()function did. 
Using list slice to easily transfer 1D list to 2D list.
for i in a rang, can not directly in a int.
'''
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        if (len(nums)*len(nums[0]) != r * c):
            return nums
        
        res = []
        for i in range(len(nums)):
            res += nums[i]
        
        ans = []
        for j in range(r):
            ans.append(res[(j*c): (j*c+c)])
        return ans

'''
there is also a cheating way which is import library to do this job, by using numpy.reshape() and tolist()
numpy.reshape(list,(row, column))
the first parameter is the array you want to reshap, the second is the new numbers of rows and colums that you want

array.tolist()
change array to a list
'''
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
            
'''
try & except
If an error is encountered, a try block code execution is stopped and transferred
down to the except block. 
'''

