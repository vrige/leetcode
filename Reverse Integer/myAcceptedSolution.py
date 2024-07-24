class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x = x * (-1)

        c = int(str(x)[::-1])
        if neg:
            c *= -1

        if c > pow(2, 31) - 1 or c < -pow(2, 31):
            c = 0
        
        return c
