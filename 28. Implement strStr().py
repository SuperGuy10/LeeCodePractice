'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        else:
            for n in range(len(haystack)):
                if needle == haystack[n:n+len(needle)]:
                    return n


'''
use find() function:
Return Value from find()
The find() method returns an integer value.
If substring exists inside the string, it returns the index of first occurence of the substring.
If substring doesn't exist inside the string, it returns -1.

find() Parameters
The find() method takes maximum of three parameters:
sub - It's the substring to be searched in the str string.
start and end (optional) - substring is searched within str[start:end]
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        return haystack.find(needle)
