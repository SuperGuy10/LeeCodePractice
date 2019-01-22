'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [0,9,1,2,4]. From the head of B, 
it reads as [3,2,4]. There are 3 nodes before the intersected node in A; 
There are 1 node before the intersected node in B.
'''

'''
This soulution is brilliant.
Since the two list may not be the same lenth, to handle that easily is to use two pointets and combine the two list together.
for ther first loop, one list will end earlier than the other, so swith the first haed to the second list which
as the result will give you a list of two input lists.
same for the second list if the second ends earlier than the first.

After two loop, they will all end because they have the same lenth.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        if headA is None or headB is None:
            return None
        
        while p1 is not p2:
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        return p1
