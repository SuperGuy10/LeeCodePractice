'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
'''

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return len(s.strip().split())

'''
solution 2
'''

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s ==''):
            return 0
        
        
        count = 0
        index =0
        l =len(s)
        Flag = False
        while( index < l):
            if(s[index] ==' ' and Flag == True):
                count+=1
                Flag = False
            elif(s[index] != ' '):
                Flag = True
            index+=1
        if(Flag ==True):
            return count +1
        elif(s[l-1] ==' '):
            return count
        else:
            return 0
