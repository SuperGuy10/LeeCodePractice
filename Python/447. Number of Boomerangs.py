'''
Given n points in the plane that are all pairwise distinct,
a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k 
(the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and
coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p1 in points:
            pdic = {}
            for p2 in points:
                d = (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 
                if d in pdic:
                    res += pdic[d] # 加完相当于1+2+3+...+(n-1)=n*(n-1) / 2
                    pdic[d] += 1
                else:
                    pdic[d] = 1
        return 2*res #所以最后ans=2*ans=n*(n-1)
