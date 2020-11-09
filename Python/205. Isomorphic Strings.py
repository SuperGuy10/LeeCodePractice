'''
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

'''
If the character appeared, show with the same number.
odd-->122
edd-->122
appedn-->122345
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        see1 = {}
        see2 = {}
        m = n = 0
        s1 = []
        s2 = []
        
        for i in s:
            if i in see1:
                s1.append(see1[i])
            else:
                see1[i] = m
                m += 1
                s1.append(see1[i])
        print(s1)
        for j in t:
            if j in see2:
                s2.append(see2[j])
            else:
                see2[j] = n
                n += 1
                s2.append(see2[j])
        print(s2)
        if s1 == s2:
            return True
        else:
            return False


'''
This idea is to match s with the value in t and match t with the value in s, then check the lenth.
eg:odd-egg: o->e d->g
also we can check if the words mathching is unique or not.
'''

class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        
        h ={}
        for i in range(len(s)):
            if s[i] not in h:
                if t[i] not in h.values():
                    h[s[i]] = t[i]
                else:
                    return False
            else:
                if h[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True

'''
zip(): to make two list as a dictionary
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

#or solution like below
        
def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))
