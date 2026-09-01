class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub_sum = []

        def dfs(index, cur_sum):
            if cur_sum == target:
                res.append(sub_sum.copy())
                return
            if index == len(nums) or cur_sum >= target:
                return
            sub_sum.append(nums[index])
            cur_sum += nums[index]    
            dfs(index, cur_sum)
            
            sub_sum.pop()
            cur_sum -= nums[index]
            dfs(index + 1, cur_sum)

        dfs(0, 0)
        return res    
            