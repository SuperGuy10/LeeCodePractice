'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        FakeHead = ListNode('FakeHead')
        FakeHead.next = head
        
        prev = FakeHead
        curr = head
        while curr:
            if curr.val != val:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
                
        return FakeHead.next        
