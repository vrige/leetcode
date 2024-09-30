class Solution:
    out = []

    def generateParenthesis(self, n: int) -> List[str]:
        
        self.out = []
        self.ricursive(n, 0,0, "")

        return self.out
    
    def ricursive(self, tot, l,r, tem):

        if l < tot:
            self.ricursive(tot,l+1,r, tem+"(")
        
        if r < tot and l > r:
            self.ricursive(tot,l,r+1, tem+")")

        if len(tem) > 2*tot:
            return None

        if len(tem) == tot * 2 and tem not in self.out:
            self.out.append(tem)
