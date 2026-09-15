class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}

        s_sorted = sorted(s)
        for char in s_sorted:
            s_dic[char] = s_dic.get(char, 0) + 1

        t_sorted = sorted(t)
        old_char = ''
        for char in t_sorted:
            if char not in s_dic:
                return False
            t_dic[char] = t_dic.get(char, 0) + 1
            if old_char in s_dic and char != old_char:
                if s_dic[old_char] != t_dic[old_char]:
                    return False
            old_char = char

        for char in s_dic:
            if char not in t_dic or s_dic[char] != t_dic[char]:
                return False    

        return True       

    
        