class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max = 0

        for ind, val in enumerate(s[:(len(s)-max)]):
            
            dictt = set()    

            for i in range(len(s[ind::])):
                if s[ind+i] not in dictt:
                    dictt.add(s[ind+i])
                else:
                    if max < len(dictt):
                        max = len(dictt)
                    break

            if max < len(dictt):
                max = len(dictt)

        return max