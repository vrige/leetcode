class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs)
        if n <= 0:
            return ""
        elif n == 1:
            return strs[0]
        
        min = float('inf')
        for i in range(0,n):
            min = min if min < len(strs[i]) else len(strs[i])

        y = sorted(strs)

        prefix = ""
        for i in range(0,len(y[0])):
            if y[0][i] == y[-1][i]:
                prefix = prefix + y[0][i]
            else:
                break

        return prefix