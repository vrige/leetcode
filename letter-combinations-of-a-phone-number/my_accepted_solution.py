class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        out = []
        p = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

        def ric(arr, inp, index):
            
            for i in arr:
                if index == len(digits) - 1:
                    out.append(inp+i)
                    continue
                    
                ric(p[digits[index + 1]], inp + i,index+1)
        
        if len(digits) > 0:
            ric(p[digits[0]],"",0)

        return out


    