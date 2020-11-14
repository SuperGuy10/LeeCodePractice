/**
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:
Input: s = "1"
Output: 1

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
*/

class Solution {
    public int numDecodings(String s) {
        HashMap<Integer, Integer> map = new HashMap<>();
       
        return helper(s,0, map);
    }
    
    public int helper(String s, int start, HashMap<Integer, Integer> map){
        if(start == s.length()){
            return 1;
        }
        if(s.charAt(start) == '0'){
            return 0;
        }
        
        int m = map.getOrDefault(start, -1);
        if(m != -1){
            return m;
        }
        
        int part1 = helper(s, start+1, map);
        int part2 = 0;
        
        if(start<s.length()-1){
            int ten = (s.charAt(start)-'0')*10;
            int one = s.charAt(start+1)-'0';
            if(ten+one<=26){
                part2 = helper(s, start+2, map);
            }
            
        }
        
        map.put(start, part1+part2);
        
        return part1+part2;
        
        
    }
    
    
}
