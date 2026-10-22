class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        break_map=[0]*(len(s)+1)
        break_map[0]=1
        for i in range(len(s)):
            element=break_map[i]
            if element == 1:
                for word in wordDict:
                    if s[i:i+len(word)]==word:
                        break_map[i+len(word)]=1
        # print(break_map)
        return break_map[-1]==1
        