class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        t = 0
        
        posx = 0
        posy = 0
        
        for i in instructions:
            if i == 'G':
                posx += dirs[t][0]
                posy += dirs[t][1]
                # print(posx, posy)
            elif i == 'L':
                t -= 1
                t %= 4
            else:
                t += 1
                t %= 4
        
        return posx == 0 and posy == 0 or t != 0