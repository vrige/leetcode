class Solution:
    def convert(self, s: str, numRows: int) -> str:

        delta = numRows - 2
        if delta < 0:
            delta = 0

        deltaX = numRows + delta
        output = ""
        
        for l in range(numRows):
            
            i = l
            while i < len(s):

                output += s[i]
                
                if l != 0 and l != (numRows-1) and (i + deltaX - 2 * l) < len(s):
                    output += s[i + deltaX - 2 * l]
                
                i += deltaX

        return output