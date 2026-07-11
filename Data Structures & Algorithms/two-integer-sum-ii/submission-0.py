class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] < numbers[i]:
                continue
            for j in range(i+1, len(numbers)):
                if numbers[j] > target-numbers[i]:
                    continue
                if numbers[j] + numbers[i] == target:
                    return [i+1, j+1]