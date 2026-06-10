class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            mem = [0]*26
            for c in word:
                mem[ord(c)-ord("a")]+=1
            mem_tuple = tuple(mem)
            if mem_tuple not in my_dict:
                my_dict[mem_tuple] = [word]
            else:
                my_dict[mem_tuple].append(word)
        return list(my_dict.values())