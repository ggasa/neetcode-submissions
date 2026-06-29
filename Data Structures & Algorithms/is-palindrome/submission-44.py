class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i_clean_s = len(s)-1
        i_start = 0 
        while i_start < i_clean_s: 
            if not s[i_start].isalnum():
                i_start +=1
            elif not s[i_clean_s].isalnum():
                i_clean_s -=1
            else:
                if s[i_start].lower() != s[i_clean_s].lower():
                    return False
                i_start +=1
                i_clean_s-=1
        return True
