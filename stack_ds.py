class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
    
    def push(self, item):
        """Add an element to the top of the stack"""
        self.items.append(item)
        print(f"Pushed {item} to stack")
    
    def pop(self):
        """Remove and return the top element from the stack"""
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from stack")
            return popped_item
        print("Stack Underflow: Cannot pop from empty stack")
        return None
    
    def display(self):
        """Display all elements in the stack (top to bottom)"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack elements (top to bottom):")
        for item in reversed(self.items):
            print(f"| {item:^5} |")  # Centered in a 5-char wide cell
        print("-------")
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def peek(self):
        """Return the top element without removing it"""
        if not self.is_empty():
            return self.items[-1]
        print("Stack is empty")
        return None


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Display stack
    stack.display()
    # Output:
    # Stack elements (top to bottom):
    # |  30  |
    # |  20  |
    # |  10  |
    # -------
    
    # Pop elements
    stack.pop()  # 30
    stack.pop()  # 20
    
    # Display after pops
    stack.display()
    # Output:
    # Stack elements (top to bottom):
    # |  10  |
    # -------
    
    # Try popping from empty stack
    stack.pop()  # 10
    stack.pop()  # Stack Underflow message