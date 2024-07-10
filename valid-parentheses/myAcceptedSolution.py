class Solution(object):
    def isValid(self, s):
    
        seen = []
        openn = {'(':')','{':'}','[':']'}

        for i in range(len(s)):

            if s[i] in openn.keys():
                seen.append(s[i])
            else:
                if seen != []:
                    c = seen.pop(-1)
                else:
                    return False
                    
                if openn[c] != s[i]:
                    return False
        
        if seen != []:
            return False
        
        return True