'''
Given two strings A and B of lowercase letters, 
return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false

Note:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
'''

'''
Return Value from zip()
The zip() function returns an iterator of tuples based on the iterable object.
If no parameters are passed, zip() returns an empty iterator
If a single iterable is passed, zip() returns an iterator of 1-tuples. Meaning, the number of elements in each tuple is 1.
If multiple iterables are passed, ith tuple contains ith Suppose, two iterables are passed; 
one iterable containing 3 and other containing 5 elements. Then, the returned iterator has 3 tuples. 
It's because iterator stops when shortest iterable is exhaused.

Example:
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']
# No iterables are passed
result = zip()
# Converting itertor to list
resultList = list(result)
print(resultList)
# Two iterables are passed
result = zip(numberList, strList)
# Converting itertor to set
resultSet = set(result)
print(resultSet)

Solution:
[]
{(2, 'two'), (3, 'three'), (1, 'one')}

'''

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): 
            return False
        if A == B and len(set(A)) < len(A): 
            return True

        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]

