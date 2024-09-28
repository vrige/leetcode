class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        max=1
        saved = s[0]
        for i in range(1,n):

            c = 1
            while i - c >= 0 and i + c <= (n-1):
                if s[i-c] == s[i+c]:
                    c += 1
                else:
                    break
            if max < 1 + 2 *(c-1):
                max = 1 + 2 *(c-1)
                saved = s[i-(c-1):i+(c-1)+1]
            
            if s[i] == s[i-1]:
                c = 1
                while i - c - 1 >= 0 and i + c <= (n-1):
                    if s[i-c-1] == s[i+c]:
                        c += 1
                    else: 
                        break
                    
                if max < 2 + 2 *(c-1):
                    max = 1 + 2 * (c-1)
                    saved = s[i-(c-1)-1:i+(c-1)+1]
            
        return saved
        