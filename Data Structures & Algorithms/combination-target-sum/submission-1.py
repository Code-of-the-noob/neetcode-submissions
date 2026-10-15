class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Overtime, needed multiple attempts at run
        """
        numbers=defaultdict(list)
        numbers[0].append([])
        for num in sorted(nums):
            for i in range(target+1):
                # print("k",numbers[target-i], target,i)
                for k in numbers[i-num]:
                    # print(i,num,k)
                    new_way=[x for x in k]+[num]
                    numbers[i].append(new_way)

        # print(numbers)
        return numbers[target]
                    