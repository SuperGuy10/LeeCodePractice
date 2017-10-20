'''
tag: Array. Difficulty: easy.
Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1] Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2] Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''

'''
for this question, the basic idea is to find the number appears most times. If there are more than one number appears the same most
times, you need to find out the smallest lenth of a subarray of nums. So an easy way to do this is you need to store the frequency, 
the first appearing positioin, the last appearing positon. For my own method is using Pyton dictionary to store all these data.
Unfortunately, this method spend a lot of time to process, only beat 6% submission.
'''

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):  #this i is int
            if nums[i] not in dic:
                dic[nums[i]] = [1,i,i]  #dic[nums[i]] means the key is nums[i]
            else:
                dic[nums[i]][0] += 1  #means the first value of the key nums[i]
                dic[nums[i]][2] = i
        dic2 = {}
        appear = []
        for j in dic:  #this j is item in dic, which equal to keys. 
            appear.append(dic[j][0])
            #print(dic[j])
        
        for j in dic:
            #print(j)
            if dic[j][0] == max(appear):
                dic2[j] = dic[j]
        #rint(dic2)
        
        position = []
        for k in dic2:
            position.append(dic2[k][2]-dic[k][1]+1)
    
        return min(position)
        
'''
For the fast solution,
'''

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        for i in nums:
            if i not in cnt:
                cnt[i] = 0
            cnt[i] += 1
        max_cnt = max(cnt.values())
        max_ints = []
        for n, v in cnt.items():
            if v == max_cnt:
                max_ints.append(n)
        min_cnt = len(nums)
        for n in max_ints:
            begin = 0
            end = len(nums)-1
            while nums[begin] != n:
                begin += 1
            while nums[end] != n:
                end -= 1
            min_cnt = min(min_cnt, end-begin+1)
            if min_cnt == max_cnt:
                return min_cnt
        return min_cnt
