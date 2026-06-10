class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memory_s = {}
        memory_t = {}
        if len(s) != len(t):
            return False
        else:
            for c in s:
                if c not in memory_s:
                    memory_s[c] = 1
                else:
                    memory_s[c] += 1
            for c in t:
                if c not in memory_t:
                    memory_t[c] = 1
                else:
                    memory_t[c] +=1
        if memory_t == memory_s:
            return True
        else:
            return False
