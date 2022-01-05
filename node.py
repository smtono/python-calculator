# Expression will have a left value, operation, and right value. 
# Read just like an actual operation, ex 8 * 8
class Expression:
    def __init__(self, left, operation, right) -> None: # Returns "None" that is the meaning
        self.left = left
        self.operation = operation
        self.right = right
    
    def evaluate(self) -> int: # Returns an int (the result/answer)
        result = 0
        if self.operation == '+':
            result = int(self.left) + int(self.right)
        elif self.operation == '-':
            result = int(self.left) - int(self.right)
        elif self.operation == '*':
            result = int(self.left) * int(self.right)
        elif self.operation == '/':
            result = int(self.left) / int(self.right)
        return result