class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        var={}
        for x in nums:
            if x in var:
                return True
            var[x]=True
        return False
        