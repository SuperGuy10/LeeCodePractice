'''
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 !=0: #can only be divided by 3
                res.append("Fizz")
            elif i%5 == 0 and i%3 !=0: #can only be divided by 5
                res.append("Buzz")
            elif i % 15 == 0:
                res.append("FizzBuzz")
            else:
                res.append(str(i))
                
        return res
        
#Solution 2: order of the if statements matters.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i %3 == 0 and i%5 == 0:
                res.append("FizzBuzz")
            elif i%5 == 0:
                res.append("Buzz")
            elif i%3 == 0:
                res.append("Fizz")
            else:
                res.append(str(i))
                
        return res
        
#Solution3:

def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
