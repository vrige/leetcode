class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        max=0
        saved = ""
        for i in range(n):
            [pal, correction, tower] = self.recursive_pal(s[i:], True, False)
            if correction and len(pal) > max:
                max = len(pal)
                saved = pal
        return saved

    def recursive_pal(self, s:str, correct: bool, tower: bool):
            
        if len(s) > 2 and s[0] == s[-1]:
            [pal, corr, tower_] = self.recursive_pal(s[1:(len(s)-1)], True, True)
            if corr:
                return [s[0] + pal + s[-1], True, tower_]
            else:
                if tower:
                    return ["", False, tower]
                else:
                    return self.recursive_pal(s[0:(len(s)-1)], True, False)
        elif len(s) > 2 and s[0] != s[-1]:
            if tower:
                return ["", False, tower]
            else:
                return self.recursive_pal(s[0:(len(s)-1)], True, False)
        elif len(s) <= 1 or (len(s) == 2 and s[0] == s[1]):
            return [s, True, tower]
        else:
            return ["", False, tower]
