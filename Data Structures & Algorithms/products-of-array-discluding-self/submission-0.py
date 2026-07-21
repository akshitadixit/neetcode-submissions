class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixprod = [1]
        suffixprod = [1]

        for i in range(len(nums)):
            prefixprod[i] = prefixprod[i]*nums[i]
            if i != len(nums)-1:
                prefixprod.append(prefixprod[i])

        for i in range(len(nums)-1):
            suffixprod[i] = suffixprod[i]*nums[len(nums)-1-i]
            suffixprod.append(suffixprod[i])

        suffixprod = suffixprod[::-1]

        print(prefixprod, suffixprod)

        output = [suffixprod[1]]
        for i in range(1, len(nums)-1):
            print(i)
            output.append(prefixprod[i-1]*suffixprod[i+1])
        output.append(prefixprod[-2])
        return output
