class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        if sum(nums)==target:
            return len(nums)
        if target in nums:
            return 1

        currSum = 0
        l = 0
        res = len(nums)


        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target and l<=r:
                res = min(res, r-l+1)
                currSum -= nums[l]
                l += 1

        return res

        