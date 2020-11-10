class Solution:
     def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0]) != r*c:
            return nums
        res = []
        res_i = 0
        res_temp = []
        for i in nums:
            for k in i:
                if res_i < c:
                    res_temp.append(k)
                    res_i += 1
                else:
                    res.append(res_temp)
                    res_temp = [k]
                    res_i = 1
        res.append(res_temp)
        return res


        

        
        