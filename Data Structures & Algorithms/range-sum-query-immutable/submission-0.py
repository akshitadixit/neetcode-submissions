class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def sumRange(self, left: int, right: int) -> int:
        currsum = 0
        prefixsum = 0

        for i in range(right+1):
            if i==left:
                prefixsum = currsum
            currsum += self.nums[i]

        return currsum - prefixsum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)