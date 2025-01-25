class Solution
    def partitionString(self, s str) - int
        if len(s)  1
            list_out = []
            out = set()
            for i in range(len(s))
                if s[i] in out
                    list_out.append(out)
                    out = set()
                    out.add(s[i])
                else
                    out.add(s[i])
                if i == len(s) - 1
                    list_out.append(out)
            return len(list_out)
        else
            if len(s) == 1
                return 1
            else
                return 0
