class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        ans_list = []
        for word in strs:
            count = [0]*26
            for l in word:
                # add count for each letter
                count[ord(l) - ord("a")] += 1
            key = tuple(count)
            if key not in ans:
                ans[key] = []
            ans[key].append(word)            
        output = [group for group in ans.values()]
        return output
        




        
        