'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?

                           ___
                         /     \
        Start____a______E       b
                        \       /
                         c__M__/   

Conditions:
1. Fast velocity is twice the Slow velocity
2. time is the same
3. assume Fast goes n rounds of the cycle, slow m rounds of the cycle,n - m = 1 (this condition is easy to be ignored, I didn't come out with the solution at first because of ignore of this equation)
Because the first time slow meets fast they are at the intersection, fast can only have one more round than slow. This is important to know.

Let's have the distance equation
Fast vs Slow
a + (b + c)n + b = 2 [a + (b + c)m + b]
(n - 2m)(b + c) = a + b
from here we know that
n = m + 1(from condition 3) and n - 2m > 0
so we have 1 - m > 0
we get the result m < 1, i.e. Slow cannot even finish one round of the cycle.

Fast and Slow have to meet when Fast finishes one cycle plus b and slow goes b around the cycle
a + (b + c) + b = 2(a + b)
so we have a = c
'''

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next            
            fast = fast.next.next
            
            # loop found
            if slow == fast:
                
                # CONCEPT:
                #
                #  When slow and fast meet, fast would have covered twice the distance
                # of slow. So,
                #
                # 2*dis_slow = dis_fast    --- 1
                #
                # Also, dis_fast - dis_slow = loop_length   --- 2
                #
                # from eqs 1 and 2,
                #
                # dis_slow = loop_length   --- 3
                #
                # Now, suppose distance till loop beginning is dis_loop_start, then,
                # slow can go a maximum of dis_loop_start + loop_length when it hits
                # loop for the first time.
                # 
                # Since, from eqn 3, slow has already traversed loop_length out of 
                # dis_loop_start + loop_length, we need to only proceed slow further
                # by, (dis_loop_start + loop_length) - loop_length = dis_loop_start
                # times before we hit the node where cycle begins. Hence, we now set
                # fast to head and continue slow further till they meet.
                fast = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                    
                return slow
        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
