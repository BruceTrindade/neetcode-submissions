class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}

        for char in s:
            s_dic[char] = s_dic.get(char, 0) + 1

        for char in t:
            if char not in s_dic:
                return False
            t_dic[char] = t_dic.get(char, 0) + 1

        for char in s_dic:
            if char not in t_dic or s_dic[char] != t_dic[char]:
                return False    

        return True       
        