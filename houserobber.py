'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        skip = 0
        take = 0
        for i in range(len(nums)):
            temp = skip
            skip = max(skip, take)
            take = temp+nums[i]
        return max(skip, take)