class Solution:
    def intToRoman(self, num: int) -> str:
        
        output = ""
        fifties = ["V","L","D"]
        decimals = ["I","X","C","M"]
        num_s = str(num)[::-1]

        for i, val in enumerate(num_s):

            if i == 3:
                output += decimals[i] * int(val)
                break
            print(int(val))
        
            if int(val) < 4:
                output += decimals[i] * int(val)
            elif int(val) == 4:
                output += (fifties[i] + decimals[i])
            elif int(val) == 5:
                output += fifties[i]
            elif int(val) <= 8:
                output += (decimals[i] * (int(val) - 5) + fifties[i])
            else:
                output += (decimals[i+1] + decimals[i])

        return output[::-1]
