class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Return a zigzag pattern coverted string"""
        
        if numRows <= 1 or len(s) <= numRows:
            return s
        
        # Determine number of columns
        remaining = len(s)
        numCols = 0
        # print("cp0.a",remaining,numCols)
        while remaining > 0:
            remaining -= numRows
            numCols += 1
            # print("cp0.b",remaining,numCols)
            for i in range(numRows-2):
                if remaining > 0:
                    numCols += 1
                    remaining -= 1
                else:
                    break
            # print("cp0.c",remaining,numCols)
        # print("cp1",numCols)
    
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
        
        # print("cp2",zigzag)
        
        return zigzag