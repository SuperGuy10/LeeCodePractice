'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
2:"abc", 3:"def", 
4:"ghi", 5:"jkl", 6:"mno", 
7:"pqrs", 8:"tuv", 9:"wxyz"}

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    '''
    #back tracking#
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
            
            
        def DFS(string):
            start = 0
            s = ""
            if int(string[start]) in dic:
                for i in dic[int(string[start])]:
                    if start+1 <= len(string):
                        s+=i+ DFS(string[start+1])
                        res.append(s)
                    return
        
        return res 
        
    '''
    def letterCombinations(self, digits):
        if not digits:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # compare to previous: use string(int) directly instead of in so no need to transform the data during program
        res = []
        self.dfs(digits, dic, 0, "", res)
        return res
    
    def dfs(self, digits, dic, index, path, res):
        print(path)
        if len(path) == len(digits): #each time can only add one digits under one number
            res.append(path)
            return 
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i+1, path+j, res)
