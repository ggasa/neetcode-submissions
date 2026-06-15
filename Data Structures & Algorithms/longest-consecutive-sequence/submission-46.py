class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        storage = set(nums)
        l_streak = 1
        
        if len(storage) == 0:
            return 0
        for num in storage:
            if (num-1) not in storage:
                if (num+1) in storage:
                    start = num
                    streak = 1
                    while (start+1) in storage:
                        start += 1
                        streak += 1
                    l_streak = max(l_streak,streak)
        return l_streak