class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i]!=prev:
                prev = nums[i]
                nums[k] = nums[i]
                k += 1

        return k