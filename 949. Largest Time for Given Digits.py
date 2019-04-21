'''
Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, 
and the largest is 23:59.  Starting from 00:00, 
a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  
If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""

Note:
A.length == 4
0 <= A[i] <= 9
'''

'''
itertools.permutations(iterable[, r])
This tool returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable, 
and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. 
So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


Look how easy it is:

    >>> name = 'Fred'
    >>> age = 42
    >>> f'He said his name is {name} and he is {age} years old.'
    He said his name is Fred and he is 42 years old.
As you see, this works pretty much like the .format() method, 
however you can directly insert the names from the current scope in the format string. 
This is much simpler than the old way, and avoids duplication:

    >>> name = 'Fred'
    >>> age = 42
    >>> 'He said his name is {name} and he is {age} years old.'.format(
    ...     name=name, age=age)
    He said his name is Fred and he is 42 years old.
Sure, you can omit the names inside the curly braces since Python 3.1, like this:

    >>> name = 'Fred'
    >>> age = 42
    >>> 'He said his name is {} and he is {} years old.'.format(name, age)
    'He said his name is Fred and he is 42 years old.'
'''

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        #return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
        k = sorted(list(itertools.permutations(A)),reverse=True)
        
        for i in k:            
            a,b,c,d = i
            su = (a*10+b)
            sd = (c*10+d) 

            if su < 24 and sd <60:
                return  f"{a}{b}:{c}{d}"
                
        return ''
