class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an element to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top element of the stack"""
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def peek(self):
        """Return the top element without removing it"""
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. No top element.")
            return None
    
    def size(self):
        """Return the number of elements in the stack"""
        return len(self.items)
    
    def __str__(self):
        """Return string representation of the stack"""
        return str(self.items)


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Pushing elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Stack after pushes:", stack)  # [10, 20, 30]
    
    # Popping elements
    print("Popped:", stack.pop())  # 30
    print("Stack after pop:", stack)  # [10, 20]
    
    # Peeking
    print("Top element:", stack.peek())  # 20
    
    # Checking size and emptiness
    print("Stack size:", stack.size())  # 2
    print("Is stack empty?", stack.is_empty())  # False
    
    # More pops
    print("Popped:", stack.pop())  # 20
    print("Popped:", stack.pop())  # 10
    print("Popped:", stack.pop())  # None (with message)
    
    print("Is stack empty now?", stack.is_empty())  # True