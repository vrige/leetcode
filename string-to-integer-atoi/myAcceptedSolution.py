class Solution:
    def myAtoi(self, s: str) -> int:

        s = s[::-1]

        numbers = {'0','1','2','3','4','5','6','7','8','9'}
        signs = {'+': True,'-': False}
        seen = False

        out = 0
        dec = -1

        for i in range(len(s)):
            if s[i] == " ":
                if i < len(s) -1 and s[i+1] != " ":
                    out = 0
                    dec = -1
                    seen = False
                continue
            elif s[i] in signs and not seen:
                if not signs[s[i]]:
                    out *= -1
                seen = True
            elif s[i] in numbers and not seen:
                dec += 1
                out += pow(10, dec) * int(s[i])
            elif seen and s[i] in numbers:
                seen = False
                out = int(s[i])
                dec = 0
            else:
                out = 0
                dec = -1
                seen = False
        
        if out >= pow(2,31) - 1:
            out = pow(2,31) - 1
        elif out <= -pow(2,31):
            out = -pow(2,31)

        return out
        