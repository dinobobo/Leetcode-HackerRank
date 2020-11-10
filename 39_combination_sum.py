class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        def isArrTar(i, arr):
            if sum(arr) == target:
                ans.append(arr)
            elif sum(arr) < target:
                for j in range(i, len(candidates)):
                    isArrTar(j, arr + [candidates[j]])                    
        isArrTar(0, [])
        return ans

ans = Solution()
res = ans.combinationSum([2,3,6,7], 7)