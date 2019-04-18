'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.
'''

class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])for i, j, k in itertools.combinations(p, 3))
        
        
'''
itertools.combinations(iterable, r)
Return r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sort order. 
So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
Elements are treated as unique based on their position, 
not on their value. So if the input elements are unique, there will be no repeat values in each combination.
'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        import itertools
        result = 0.0
        for a,b,c in itertools.combinations(points,3):
            area = abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))/2.0 
            if area>result:
                result = area
        return result
