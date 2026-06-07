class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = array of strings.
        result = []
        storage = {}
        for word in strs:
            unique_letters = tuple(sorted(word)) # why should we use a tuple instead of a list?
            # lists are unhasable - it's dynamic. ONLY STATIC arrays are hashable!!
            if unique_letters in storage.keys():
                storage[unique_letters].append(word)
            else:
                storage[unique_letters] = [word]
            # group same unique_letters together
        result = [val for val in storage.values()]
        return result
            