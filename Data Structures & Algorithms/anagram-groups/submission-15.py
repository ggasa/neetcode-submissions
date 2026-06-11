class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = {}

        for word in strs:
            tracker = [0]*26
            for l in word:
                num = ord(l) - ord("a")
                tracker[num] += 1
                
            tp_tracker = tuple(tracker)
            if tp_tracker not in memory:
                memory[tp_tracker] = [word]
            else:
                memory[tp_tracker].append(word)
        output = list(memory.values())

        return output
            

