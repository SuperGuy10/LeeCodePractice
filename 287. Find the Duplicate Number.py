'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        #fast = nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
        
'''
for array A = [2,6,4,1,3,1,5]
index 0 , 1, 2, 3, 4, 5, 6
value:2, 6, 4, 1, 3, 1, 5
transform to : 0 - > 2 - > 4 -> 3 -> 1 -> 6 -> 5-> [1- >6-> 5 ->1 circle] take it as circled linked list
slow = nums[slow] ===> slow = slow.next
fast = nums[nums[fast]] ===> fast = fast.next.next
'''
