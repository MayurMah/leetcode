class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Return a zigzag pattern converted string. Refer https://leetcode.com/problems/zigzag-conversion/"""
        
        if numRows <= 1 or len(s) <= numRows:
            return s
        
        # Determine number of columns
        remaining = len(s)
        numCols = 0
        while remaining > 0:
            remaining -= numRows
            numCols += 1
            for i in range(numRows-2):
                if remaining > 0:
                    numCols += 1
                    remaining -= 1
                else:
                    break

        i = 0
        j = 0
        down = True
        arr = [['' for i in range(numCols)] for j in range(numRows)]
        for curChar in s:
            if i == 0:
                down = True
            if i == numRows-1:
                down = False
            
            arr[i][j] = curChar
            
            if down: 
                i += 1
            else:
                i -= 1
                j += 1
            
        zigzag = ''.join([''.join(x) for x in arr]) 

        return zigzag
