class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = [l for l in s if l.isalnum()]

        # In this problem you actually care about the order...can't use hashmapping
        for i,l in enumerate(s):
            print(f"index: {i}, value: {l}")
            print(f"m index: {-i}, value: {s[-i-1]}")
            if l != s[-i-1]:
                return False
            
        return True
