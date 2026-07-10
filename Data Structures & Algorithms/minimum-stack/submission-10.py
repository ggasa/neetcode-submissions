class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        # going to need to push to the main stack regardless
        self.stack.append(val) 
        if self.min_stack and self.min_stack[-1] <= val: #min_stack is not empty, we need to compare
            self.min_stack.append(self.min_stack[-1])
        else:  # min_stack is empty
            self.min_stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
