class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        else: 
            for c in s:
                if c in count_s.keys():
                    count_s[c] += 1
                else:
                    count_s[c] = 1

            for c in t:
                if c in count_t.keys():
                    count_t[c] += 1
                else:
                    count_t[c] = 1
            if count_s == count_t:
                return True
            else:
                return False
