class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxi = 0
        left = 0
        index = {}


        for i in range(len(s)):
            if s[i] in index and index[s[i]] >= left:
                left = index[s[i]] + 1

            index[s[i]] = i
            maxi = max(maxi, i - left + 1)

        return maxi