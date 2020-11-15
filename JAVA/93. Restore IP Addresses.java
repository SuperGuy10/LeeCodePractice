/**
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. 
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

0 <= s.length <= 3000
s consists of digits only.
*/

class Solution {
//     public List<String> restoreIpAddresses(String s) {
//         List<String>ans = new ArrayList<String>();
//         int l = s.length();
//         if(l > 12 || l < 4){
//             return ans;
//         }
        
//         for(int i = 1; i<4 && i<l-2; i++){
//             for(int j = i+1; j<i+4 && j<l-1; j++){
//                 for(int k = j+1; k<j+4&& k<s.length(); k++){
//                     String s1 = s.substring(0,i);
//                     String s2 = s.substring(i,j);
//                     String s3 = s.substring(j,k);
//                     String s4 = s.substring(k,l);
                    
//                     if(check(s1)&&check(s2)&&check(s3)&&check(s4)){
//                         ans.add(s1+"."+s2+"."+s3+"."+s4);
//                     }
//                 }
//             }
//         }
//         return ans;
        
//     }
    
//     public boolean check(String s){
//         if((s.charAt(0)=='0' && s.length()>1) || Integer.parseInt(s)>255){
//             return false;
//         }else{
//             return true;
//         }
//     }
    
    public List<String> restoreIpAddresses(String s) {
        List<String>ans = new ArrayList<String>();
        int l = s.length();
        if(l > 12 || l < 4){
            return ans;
        }
        
        
        helper(s,new StringBuilder(), 0, ans, 0);
        
        return ans;
        
    }
    
    public void helper(String s, StringBuilder sb, int start, List<String> ans, int count){
        if(start == s.length()){
            if(count == 4){
                ans.add(new String(sb.substring(0, sb.length()-1)));
            }
            return;
        }
        
        if(start > s.length() || count == 4){
            return;
        }
        
        StringBuilder before = new StringBuilder(sb);
        
        sb.append(s.charAt(start)+""+".");
        helper(s, sb, start+1, ans, count+1);
        
        if(s.charAt(start) == '0'){   
            return;
        }
        
        if(start+1<s.length()){
            sb = new StringBuilder(before);
            sb.append(s.substring(start, start+2)+""+".");
            helper(s, sb, start+2, ans, count+1);
        }
        
        if(start+2<s.length()){
            sb = new StringBuilder(before);
            int value = Integer.parseInt(s.substring(start, start+3));
            if(value>=0 && value<=255){
                sb.append(s.substring(start, start+3)+""+".");
                helper(s, sb, start+3, ans, count+1);
            }
        }
        
       
    }
    
    
}
