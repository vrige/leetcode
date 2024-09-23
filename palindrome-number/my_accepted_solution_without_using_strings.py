class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        y = x
        n = 1
        while y >= 10:
            n += 1
            y = y // 10

        y = x
        lit = 0
        for i in range(n,n//2,-1):
            big = y // pow(10,i-1)
            lit = (y % pow(10, n - i + 1)) // pow(10, n - i)
            y = y - big * pow(10,i-1) - lit * pow(10, n - i)
            if big != lit:
                return False
        
        return True

