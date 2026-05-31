class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        for l in s:
            if l in dict_s.keys():
                dict_s[l] += 1
            else:
                dict_s[l] = 1
        
        for l in t:
            if l in dict_t.keys():
                dict_t[l] += 1
            else:
                dict_t[l] = 1
        
        if dict_s == dict_t:
            return True
        else:
            return False

