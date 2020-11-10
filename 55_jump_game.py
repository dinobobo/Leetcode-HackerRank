class Solution:
    def canJump(self, nums):
        memo = [0 for _ in range(len(nums))]
        memo[-1] = 1
        
        for i in range(len(nums) - 2, -1, -1):
            position_f = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, position_f + 1):
                if memo[j] == 1:
                    memo[i] = 1
                    break
        return memo[0] == 1


ans = Solution()
ans.canJump([2,3,1,1,4])