'''
Tag: Array; Difficulty: Easy.
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
        	if i in {'[','{' ,'('}: #faster way than if i == '{'
        		stack.append(i)
        	else:
        		if len(stack) == 0:
        			return False
        		top = stack.pop()
        		if i == ']' and top != '[': #no need for ] to get in stack
        			return False
        		if i == '}' and top != '{':
        			return False
        		if i == ')' and top != '(':
        			return False
        if len(stack) != 0:
        	return False
        return True  #to avoid empty stack

    
    
'''
second solution
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        query_str = None

        for i in range(len(s)):
            s_str = s[i]

            if query_str is None:
                query_str = s_str

            elif s_str == '(' or s_str == '[' or s_str == '{':
                query_str += s_str

            elif len(query_str) == 0:
                return False

            elif (s_str == ')' and query_str[-1] == '(') or \
                    (s_str == ']' and query_str[-1] == '[') or \
                    (s_str == '}' and query_str[-1] == '{'):
                query_str = query_str[:-1]

            else:
                return False

        return len(query_str) == 0
    
    
'''
fastest solution
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = False
        current = []
        op = {"[", "(", "{"}
        cl = {"]", ")", "}"}
        pairs = {"()", "{}", "[]"}
        for b in s:
            if b in op:
                current.append(b)
            else:
                try:
                    cb = current.pop()
                    pair = cb + b
                    if pair not in pairs:
                        return False
                    else:
                        continue
                except IndexError:
                    return False
        if len(current) > 0:
            return False
        return True
