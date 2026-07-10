class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        for i in range(len(nums)):
            vals[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in vals and vals[target - nums[i]]!=i:
                return [i, vals[target - nums[i]]]