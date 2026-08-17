# h = max hours koke have  
# k = bannas / hour
#    piles[i] / h
#  
#   max_b = max(piles) ? 
#   bannas_phour = [0..max_b]
#   
#piles=[3,6,7,11]
#h=8
# 3 -> mid =6 -> housr = 6 
# mid = 4 -> 3/4 = 1, 6/4 = 2, 7/4 = 2, 11/4=3 => hours = 8 
#
#
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimun_b, max_bananas = 1, max(piles)
        minimun_bananas_hour = max_bananas
        minimun_hours = h
        
        while minimun_b <= max_bananas:
            banna_per_hour = (minimun_b + max_bananas) // 2
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / banna_per_hour)
            if hours <= h and banna_per_hour <= minimun_bananas_hour:
                minimun_bananas_hour = banna_per_hour    
                minimun_hours = hours
                max_bananas = banna_per_hour - 1
            else: 
                minimun_b = banna_per_hour + 1

        return minimun_bananas_hour        
