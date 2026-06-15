class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 1

        if len(store) == 0:
            return 0   

        for num in store:
            if (num-1) not in store:
                if (num+1) in store:
                    start = num
                    sequence = 1
                    while (start+1) in store:
                            sequence +=1
                            start += 1
                    longest = max(longest, sequence)

        return longest