class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        group = set() # Using a set directly prevents duplicates automatically
        
        # 1. Loop through every possible "first" number
        for i in range(len(nums)):
            target = -nums[i]
            seen = set() # Tracks numbers available AFTER index i
            
            # 2. Pair it up with a "second" number
            for j in range(i + 1, len(nums)):
                # We need: nums[j] + third_number = target
                third_number = target - nums[j]
                
                # 3. If we've seen the required third number in this pass, we found a match!
                if third_number in seen:
                    potential_list = tuple(sorted([nums[i], nums[j], third_number]))
                    group.add(potential_list)
                    
                # Store the current number as "seen" for future pairings in this loop
                seen.add(nums[j])
                
        # Convert set of tuples back to a list of lists for LeetCode
        return [list(triplet) for triplet in group]