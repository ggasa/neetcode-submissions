class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_s = set(s)
        unique_t = set(t)
        
        combined = s+t
        unique_st = set(combined)

        for l in unique_st:
            original_count = s.count(f'{l}')
            combined_count = combined.count(f'{l}')
            if unique_s == unique_t:
                if original_count*2 != combined_count:
                    output = False
                else:
                    output = True
            else:
                output = False
        return output