'''
In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

Example 1:
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:
Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000
'''

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        tem = []
        count = 0
        ans = []
        for i in range(len(S)):
            if tem == []:
                tem += S[i],i
                #print("0",tem)
                count += 1
            else:
                if S[i] in tem:
                    count += 1
                    if i == len(S)-1 and count>=3: # for the last round, add to ans if count>3
                        ans.append([tem[1],tem[1]+count-1])
                else:
                    if count<3:
                        count = 1
                        tem = []
                        tem += S[i],i
                        #print("1", tem)
                        
                    else:
                        ans.append([tem[1],tem[1]+count-1])
                        count = 1
                        tem = []
                        tem += S[i],i
                        #print("2",tem)
        return ans


# clever way!!!!!

def largeGroupPositions(self, S):
        i, j, N = 0, 0, len(S)
        res = []
        while i < N:
            while j < N and S[j] == S[i]: j += 1
            if j - i >= 3: res.append((i, j - 1))
            i = j
        return res
