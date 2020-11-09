'''
Tag: Array; Difficulty: Easy.
Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.

'''
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        To make things easier, take three elements together.
        if f[i]==0, the middle one has to be zero to plant flower;
        i==0 or f[i-1]==0, the previous one has to be zero and incase i is the first one;
        i==f.size-1 or f[i+1]==0，the next one has to be zero and incase i is the last one;
        only when meet three conditions above at the same time, we count onece.
        and change to f[i]==1，n-
        When finally go through all the elements, if n<=0，we done, return true, otherwise false.

        """
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        return n<=0
