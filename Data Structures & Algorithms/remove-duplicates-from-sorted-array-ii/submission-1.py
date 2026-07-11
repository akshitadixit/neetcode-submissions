class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        prevcnt = 0
        for i in range(0, len(nums)):
            if nums[i]!=nums[i-1]:
                prevcnt = 1
            else:
                prevcnt += 1
            
            if prevcnt<=2:
                nums[k] = nums[i]
                k += 1

        return k