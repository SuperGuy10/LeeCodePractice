'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. 
You may return the list in any order.

Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]

Note:
0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
'''

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        '''
        C = []
        A = list(A.split())
        B = list(B.split())
        for i in range(len(A)):
            if A[i] not in A[i+1:len(A)] and A[i] not in B:
                C.append(A[i])
                print(C)
        for m in range(len(B)):
            if B[m] not in B[m+1:len(B)] and B[m] not in A:
                C.append(B[m])
                
        return C
        '''
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]

# second solution
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        uncommon = {}
        
        for word in (A+" "+B).split(' '):
            if word == "":
                continue
            elif word in uncommon:
                uncommon[word] +=1
            else:
                uncommon[word] = 1
            
        return [x for x in uncommon if uncommon[x] == 1]
