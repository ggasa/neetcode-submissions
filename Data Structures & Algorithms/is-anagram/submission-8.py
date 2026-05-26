class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapp = {}
        mapp2 = {}
        for l in s:
            if l in mapp.keys():
                mapp[l] += 1
            else: 
                mapp[l] = 1
        print(mapp)
        for l in t:
            if l in mapp2.keys():
                mapp2[l] += 1
            else: 
                mapp2[l] = 1

        if mapp==mapp2:
            return True
        else:
            return False