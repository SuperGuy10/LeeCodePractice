'''
A robot on an infinite grid starts at point (0, 0) and faces north.  
The robot can receive one of three possible types of commands:
-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 
The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
If the robot would try to move onto them, the robot stays on the previous grid square instead
(but still continues following the rest of the route.)
Return the square of the maximum Euclidean distance that the robot will be from the origin.

Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)

Example 2:
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

Note:
0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
'''


'''
Firstly, robot doesn't face north as stated in the explanation. 
When i consider north, i imagine robot faces upwards but its initial direction is to right actually.
Note: This is a similar question to Robot Room cleaner (No: 489).
Code explanation:
At first, we should make obstacles as set for O(1) check for obstacles and we simply move according to command if there is no obstacle.
Critical part is the move array in my opinion. 
It is a simplified move to next i and j in array form for "right", "up", "left", "down" respectively.
We also change d variable, which is direction variable as move index, when we get -2 or -1 command.
If command is -2, we should turn left, which is to increment direction index.
If command is -1, we should turn right, which is to decrement direction index.
Else, we can walk through untill face an obstacle or not.
And we update mx value in each move also.
'''

class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set([(x, y) for x, y in obstacles])

        di = 0
        x, y = 0, 0
        ans = 0
        for command in commands:
            if command == -1:
                di = (di + 1) % 4
            elif command == -2:
                di = (di - 1) % 4
            else:
                for step in range(command): #check if each step's result in bostacles 
                    nx, ny = x + directions[di][0], y + directions[di][1]
                    if (nx, ny) not in obstacles:
                        x, y = nx, ny
                        ans = max(ans, x ** 2 + y ** 2)
                    else:
                        break
        return ans
