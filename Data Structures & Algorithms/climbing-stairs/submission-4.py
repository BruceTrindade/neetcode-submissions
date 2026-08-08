class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = n
        memo = [-1] * stairs

        def climb_ways(way: int) -> int:
            if way >= stairs:
                return way == stairs
            if memo[way] != -1:
                return memo[way]
            memo[way] = climb_ways(way + 1) + climb_ways(way + 2)    

            return memo[way] 

        return climb_ways(0)