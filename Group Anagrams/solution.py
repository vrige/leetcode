class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = defaultdict(list)
        for j in strs:
            sort_j = ''.join(sorted(j))
            output[sort_j].append(j)
        return list(output.values())