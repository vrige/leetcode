class Solution:
    def romanToInt(self, s: str) -> int:

        dictt = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        output = 0
        skip = False

        for i, val in enumerate(s):

            if skip:
                skip = False
                continue

            if i + 1 < len(s) and dictt[val] < dictt[s[i+1]]:
                output += (dictt[s[i+1]] - dictt[val])
                skip = True
            else:
                output += dictt[val]

        return output