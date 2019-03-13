'''
Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add, 
return the element representing the kth largest element in the stream.

Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.
'''

'''
We can build a MinHeap that contains only k largest elements.
On add:
compare a new element x with min to decide if we should pop min and insert x
take into account a case when heap_size is less than k
Construction is simply calling the add function N times.

Time complexity:
Construction: O(N * logK)
Adding: O(logK)
Additional memory:
O(K) (can be reduced to O(1) by reusing memory of the existing array)
'''

class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
