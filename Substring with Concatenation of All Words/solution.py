class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        if len(words) == 0:
            return []
        n_1 = len(words[0])
        possible_output = None
        output = []

        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        for i in range(0, n - (n_1 * len(words)) + 1, 1):
            
            seen = defaultdict(int)
            if s[i:i+n_1] not in word_count:
                continue
            possible_output = i
            seen[s[i:i+n_1]] += 1
            
            for l in range(1,len(words)):
                next = i + l * n_1
                word = s[next:next+n_1]

                if word not in word_count:
                    break
                else:
                    seen[word] += 1
                    if seen[word] > word_count[word]:
                        break
            
            else:
                output.append(possible_output)
                continue

        return output