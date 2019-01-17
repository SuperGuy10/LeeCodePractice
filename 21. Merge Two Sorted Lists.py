'''
Tag: List; Difficulty: Easy.

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0) #create a new linked list
        current = head
        if l1 == None and l2 == None: #if both l1 and l2 are empty, return None directly
            return None
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1 == None: #since tow lists may have different lenth, each one has a chance to finish faster than the other.
            current.next = l2
        if l2 == None:
            current.next = l1
        return head.next
        
