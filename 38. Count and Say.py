'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

'''
'''
First solution using recursion to solve
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # s = '1'
        # for i in range(n-1):
        #     s = self.countString(s)
        # return s
        return self.countString(n)
        
        
    def countString(self, n):
        if n == 1:
            return '1'
        string = self.countString(n-1)
        result = ""
        count = 0
        for i in range(len(string)):
            if i == 0 or string[i] == string[i-1]:
                count += 1
            else:
                result = result + str(count) + string[i-1]
                count = 1
            if i == len(string)-1:
                result = result + str(count) + string[i]
        return result
        
        
'''
Second solution using "".join()
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s
