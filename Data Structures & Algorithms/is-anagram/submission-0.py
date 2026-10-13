class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1_counter=Counter(s)
        word2_counter=Counter(t)

        if not ((word1_counter-word2_counter) or (word2_counter - word1_counter)):
            return True
        return False