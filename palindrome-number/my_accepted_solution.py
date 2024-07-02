class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        lenn = len(str_x) // 2 + len(str_x) % 2
        output = True
        for i in range(lenn):
            print(i)
            if str_x[i] != str_x[len(str_x) -i -1]:
                output = False
                break
        return output