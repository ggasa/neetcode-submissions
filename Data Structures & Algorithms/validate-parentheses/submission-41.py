class Solution:
        def isValid(self, s: str) -> bool:
                par_dict = {")":"(","}":"{","]":"["}
                stack = []
                for par in s:
                        if par in par_dict.keys():
                                if stack == []:
                                        return False
                                        
                                print(f"current stack: {stack}")
                                if stack[-1] == par_dict[par]:
                                        stack.pop()
                                else:
                                        return False
                        else:
                                stack.append(par)
                if stack == []:
                        out = True
                else: 
                        out = False

                return out






