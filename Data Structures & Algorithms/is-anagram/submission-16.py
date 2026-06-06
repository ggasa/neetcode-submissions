class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict_s = {}
        dict_t = {}
        for l_s, l_t in zip(s,t):
            if l_s in dict_s:
                dict_s[l_s] += 1
            else: 
                dict_s[l_s] = 1
            if l_t in dict_t:
                dict_t[l_t] += 1
            else:
                dict_t[l_t] = 1
        if dict_s == dict_t:
            return True
        else:
            return False
            