class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_s = s.lower()
        clean_s = [char for char in l_s if char.isalnum()]
        
        i_clean_s = len(clean_s)-1
        i_start = 0 
        while i_start < i_clean_s:
            if clean_s[i_clean_s] == clean_s[i_start]:
                i_clean_s -= 1
                i_start += 1
            else:
                return False
        return True
