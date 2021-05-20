class Solution:
    def solve(self, rooms, target):
        for i in range(0,len(rooms)):
            if rooms[i] >= target:
                value = rooms[i]
                break
        else:
            return(-1)
        return(value)