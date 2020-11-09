'''
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.
Now, you are given positions of houses and heaters on a horizontal line, 
find out minimum radius of heaters so that all houses could be covered by those heaters.
So, your input will be the positions of houses and heaters seperately, 
and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
 

Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
'''

'''
Each house is either heated by the heater before it or by the heater after it, 
and the min of them is the radius required by that house, 
and the max of the radius required by each house is the answer we need. 
The special case is the house does not have a heater before it or a heater after it.
O(N)= N * logN
'''
class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        radius = 0
        i = 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            if i == 0:
                radius = max(radius, heaters[i] - house)
            elif i == len(heaters):
                return max(radius, houses[-1] - heaters[-1])
            else:
                radius = max(radius, min(heaters[i]-house, house-heaters[i-1]))
        return radius


'''        
The idea is that for every house, you want to find the closest 2 heaters, 
and whichever in the 2 that is closer should warm this house. 
Iterate through the houses, use binary search to find the closest 2 heaters, update answer.
'''
class Solution(object):
    def findRadius(self, houses, heaters):
        
        heaters.sort()
        
        ans = 0
        
        for h in houses:
            hi = bisect.bisect_left(heaters, h)
            left = heaters[hi-1] if hi-1 >= 0 else float('-inf')
            right = heaters[hi] if hi < len(heaters) else float('inf')
            ans = max(ans, min(h-left, right-h))
            
        return ans
