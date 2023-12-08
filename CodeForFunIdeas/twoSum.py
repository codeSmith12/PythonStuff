class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answerIndex = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

nums = [2,7,11,15]
target = 13

sol = Solution()

print(sol.twoSum(nums, target))