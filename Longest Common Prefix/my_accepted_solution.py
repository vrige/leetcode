class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minLen = float('inf')
        minLenWord = ""
        # check length > 0
        for word in strs:
            if len(word) == 0:
                return ""
            if minLen > len(word):
                minLen = len(word)
                minLenWord = word
        
        results = ""
        for i in range(minLen):
            for word in strs:
                if word[i] != minLenWord[i]:
                    return results
            results += minLenWord[i]
        return results