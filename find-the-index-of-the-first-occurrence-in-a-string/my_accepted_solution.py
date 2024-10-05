class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(haystack)
        m = len(needle)
        if n >= m:
            for i,v in enumerate(haystack):
                if n - i >= m and v == needle[0]:
                    s = i + 1
                    corr = True
                    for j in needle[1:]:
                        if haystack[s] != j:
                            corr = False
                        s += 1
                    if corr:
                        return i
            
        return -1