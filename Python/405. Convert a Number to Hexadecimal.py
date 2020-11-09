'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. 
If the number is zero, it is represented by a single zero character '0'; otherwise, 
the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:
Input:
26
Output:
"1a"

Example 2:
Input:
-1
Output:
"ffffffff"


'''
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        if num > 0:
            ans = ''
            while num > 0:
                m = num & 15
                ans = digits[m] + ans
                num = num >> 4

            return ans
        else:
            num = n2_32 + num
            return self.toHex(num)

digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
n2_32 = 2 ** 32

'''
l = [] #此法只能转正数
        m={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        while num / 16:
            t = num%16
            #print(t)
            if t > 9:
                l.append(m[t])
            else:
                l.append(t)
            num = int(num / 16)
        l.reverse()
        print(l)
        return ''.join('%s' % id for id in l)'''
'''
要将一个十进制数转换为十六进制数，不管其是正数还是负数，都只需要将其二进制表示
每四位分成一个单元，将其取出后计算这四位二进制数代表的十进制数，与0~f之间的数字
做一个映射即可。要把每四位取出也很简单，与0xf进行AND运算即可。 
在C++中，左移是逻辑移位，也就是说在数字后面补0，右移运算符是算术移位，也就是在
左侧补符号位(正数补0，负数补1
'''
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        m = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        if(num == 0): 
            return "0"
        while(num != 0 and len(s) < 8):#len(s) < 8表示最大的十六进制数的位数（0xFF FF FF FF）
            s = m[num & 0xf] + s
            print(num & 0xf)
            num = num >> 4
            #print(num)
        return s[::1]

