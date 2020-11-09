'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to closest person.

Example 1:
Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Note:
1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
'''


'''
We iterate i over range(len(seats)), and initialize prev = None, 
which records the index of the previous 1, and the solution of the problem res = -float('inf'). 
If seats[i] == 1, and prev == None, 
it means that we encounter the first seated person (e.g., we meet the 1 in such configuration [0,0,1,....]), 
then the current largest distance is i, which can be achieved by sitting at the leftmost seat, 
and we update res = i, prev = i. If seats[i] == 1, and prev != None, 
it means that we encounter at least two persons already (e.g., we meet the second 1 in such configuration [...,1,0,0,0,1,...]), 
the by sitting in the middle of the i and prev, we maximize the minimum distance between the nearest person, which is (i-prev) // 2, 
we update res = max(res, (i-prev) // 2), and prev = i. Finally, after iterating i over range(len(seats)), 
we also need to consider the possibility of sitting at the rightmost seat (e.g., in such configuration [...,1,0,0,0]), 
and we need to make a final update of res by res = max(res, len(seats)-1-prev). Then we return res.
Time complexity: O(n), space complexity: O(1).
'''

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev = -1
        res = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == -1:
                    res = i
                    prev = i
                else:
                    res = max(res, (i-prev) // 2)
                prev = i
        res = max(res, len(seats)-1-prev)
        return res
