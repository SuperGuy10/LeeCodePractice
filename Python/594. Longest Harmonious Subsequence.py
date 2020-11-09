'''
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''

# dictionary is orderless,

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        order = sorted(dic.items())
        
        result = []
        
        for i in range(len(order)-1):
            if order[i+1][0] - order[i][0] == 1:
                result.append(order[i+1][1] + order[i][1])
        if result == []:
            return 0
        else:
            return max(result)


'''
Update my code with this idea.
class Solution:
    def findLHS(self, nums: 'List[int]') -> 'int':
        
        count = collections.Counter(nums)
        sets = set(nums)
        ans = 0
        for i in sets:
            if i+1 in sets:
                ans = max(ans,count[i]+count[i+1])
        return ans
'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        ans = 0
        for i in dic: #try to find item in dict instead of based on index cause dictionary is orderless
            if i+1 in dic:
                ans = max(ans,dic[i]+dic[i+1])
        return ans
