'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. 
If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3, because by repeating A three times (“abcdabcdabcd”), 
B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        C = ""
        for i in range(len(B)/len(A) + 3): 
            if B in C:
                return i
            C += A
        return -1


'''
why 3 here? let me explain:

i can only take value up to len(B)/len(A)+2 due to python range function
it is integer division, e.g. len(B) is 3, len(A) is 2, len(B)/len(A) gives you 1 only, you need to repeat A at least len(B)/len(A)+1 times for B being possible as substring of A (len(A)>=len(B)).
if A repeated len(B)/len(A) +1 times and B is its substring, then B is also a substring if A repeated len(B)/len(A) +2 times
if A repeated len(B)/len(A) +2 times and B is NOT substring of it, there is no point of repeating more times to check
'''
