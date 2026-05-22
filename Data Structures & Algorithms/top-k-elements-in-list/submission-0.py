class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = int array
        # k = int, top k freq elements
        tracker = {}
        top_k = []

        for i,num in enumerate(nums):
            # if num already exists in the tracker
            if num in tracker.keys():
                tracker[num]+=1
            else:
                tracker[num] = 1

        print(tracker)        
        while k >= 1:
            tracker_value = max(tracker, key=tracker.get)
            tracker.pop(tracker_value)
            top_k.append(tracker_value)
            k-=1
        return top_k