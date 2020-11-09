'''
In a list of songs, the i-th song has a duration of time[i] seconds. 
Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 
Note:
1 <= time.length <= 60000
1 <= time[i] <= 500
'''


'''
Observe that (a + b) mod m = a mod m + b mod m. Then if we mod all values in time array by 60, the answer don't change.
For example [30, 40, 20, 90, 100, 80] would be [30, 40, 20, 30, 40, 20].
Then if 0 is in the modified array with count1, all pairs of 0 would be valid. The count is count1 * (count1 - 1) / 2.
If 30 is in the modified array with count2, all pairs of 30 would be valid. The count is count2*(count2 - 1) /2
If key is in modified array with count3, all pairs of key and (60 - key) would be valid (If 60 - key is in the modified array too). 
The count is count3 * count4 (where count4 is the number of times 60 - key appears in the modified array. 
To eliminate duplicate count, we keep key >0 and key < 30).
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import defaultdict
        songs = defaultdict(int)
        for song in time:
            songs[song%60] +=1
        count = songs[0] * (songs[0]-1) / 2
        count += songs[30] * (songs[30]-1) / 2
        for i in range(1,30):
            count += songs[i] * songs[60-i]
        return int(count)


'''
Calculate the time % 60 then it will be exactly same as two sum problem.
t % 60 gets the remainder 0 ~ 59.
We count the occurrence of each remainders in a array/hashmap c.
we want to know that, for each t, how many x satisfy (t + x) % 60 = 0.
t % 60 + x % 60 = 60 for the most cases.
It has to be noticed that, if t % 60 = 0, x % 60 = 0 instead of 60.
60 - t % 60 will get a number in range 1 ~ 60.
(60 - t % 60) % 60 can get number in range 0 ~ 59
'''

def numPairsDivisibleBy60(self, time):
    c = collections.Counter()
    res = 0
    for t in time:
        res += c[-t % 60]
        c[t % 60] += 1
    return res
