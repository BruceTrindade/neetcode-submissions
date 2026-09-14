class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        result = []

        for index, num in enumerate(nums):
            dic[num] = index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in dic and dic[diff] != index:
                return [index, dic[diff]]

        return []                