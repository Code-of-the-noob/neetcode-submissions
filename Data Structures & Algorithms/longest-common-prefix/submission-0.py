class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word1 = strs[0]

        for word2 in strs[1:]:
            if len(word2) < len(word1):
                word1, word2 = word2, word1
                
            for i, v in enumerate(word1):
                if word2[i] != v:
                    word1 = word1[:i]

        return word1
