class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = {}
        for word in strs:
            count = [0]*26
            for letter in word:
                num = ord(letter) - ord("a")
                count[num] +=1
            
            key = tuple(count)
            if key not in memory:
                memory[key] = [word]
            else:
                memory[key].append(word)
        output = [val for val in memory.values()]
        return output