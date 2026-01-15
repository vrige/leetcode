class Solution:
    def countAndSay(self, n: int) -> str:
        input = "1"
        if n == 1:
            return input
        for i in range(n-1):
            input = self.rle(input)
        return input

    def rle(self, n: str) -> str:
        temp = n[0:1]
        count = 0
        output = ""
        for t, i in enumerate(n):
            if i == temp:
                count += 1
            else:
                output += str(count) + temp
                count = 1
                temp = i
            if len(n) - 1 == t:
                output += str(count) + temp
        return output
            