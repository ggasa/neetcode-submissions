class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = {}
        for num in nums:
            if num in mapp.keys():
                mapp[num] += 1
            else:
                mapp[num] = 1
        print(mapp.values())
        if sum(mapp.values())== len(mapp.values()):
            out = False
        else:
            out = True
        return out