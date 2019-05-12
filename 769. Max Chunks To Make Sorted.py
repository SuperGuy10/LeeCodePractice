'''
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], 
we split the array into some number of "chunks" (partitions), and individually sort each chunk.  
After concatenating them, the result equals the sorted array.
What is the most number of chunks we could have made?

Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:
arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
'''
'''
The key to understand this algorithms lies in the fact that when max[index] == index, 
all the numbers before index must be smaller than max[index] (also index), 
so they make up of a continuous unordered sequence, i.e {0,1,..., index}. 
This is because numbers in array only vary in range [0, 1, ..., arr.length - 1], 
so the most numbers you can find that are smaller than a certain number, 
say arr[k], would be arr[k] - 1, i.e [0, 1, ..., arr[k] - 1]. So when arr[k] is the max number in [arr[0], arr[1], ..., arr[k]],
all the k - 1 numbers before it can only lies in [0, 1, ..., arr[k] - 1], so they made up of a continuous sequence. 
(You can also prove it using contradiction, which may be easier to understand)
'''

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = mx = 0
        for i,x in enumerate(arr):
            mx = max(mx,x)
            if i == mx:
                ans+=1
        return ans
