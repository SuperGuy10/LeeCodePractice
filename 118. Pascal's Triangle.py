'''
Tag: Array; Difficulty: Easy.
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

'''
be careful with 2D list initialization.

for i in range(Rows):
    list = [[1]*(i+1)]
print(list)
above will over write list

list = ([[1]*(i+1)]for i in range(Rows))
print(list)
'''
def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
