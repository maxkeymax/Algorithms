class Queue:
    def __init__(self):
        """Initialize an empty queue"""
        self.items = []
    
    def enqueue(self, item):
        """Add an element to the end of the queue"""
        self.items.append(item)
        print(f"Enqueued {item} to queue")
    
    def dequeue(self):
        """Remove and return the element from the front of the queue"""
        if not self.is_empty():
            dequeued_item = self.items.pop(0)
            print(f"Dequeued {dequeued_item} from queue")
            return dequeued_item
        print("Queue Underflow: Cannot dequeue from empty queue")
        return None
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of elements in the queue"""
        return len(self.items)
    
    def display(self):
        """Display all elements in the queue (front to rear)"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Queue elements (front → rear):")
        print("Front →", " → ".join(map(str, self.items)), "→ Rear")


# Example usage
if __name__ == "__main__":
    q = Queue()
    
    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    # Display queue
    q.display()
    # Output:
    # Queue elements (front → rear):
    # Front → 10 → 20 → 30 → Rear
    
    # Dequeue elements
    q.dequeue()  # 10
    q.dequeue()  # 20
    
    # Display after dequeues
    q.display()
    # Output:
    # Queue elements (front → rear):
    # Front → 30 → Rear
    
    # Check size and emptiness
    print("Queue size:", q.size())  # 1
    print("Is queue empty?", q.is_empty())  # False
    
    # Final dequeue
    q.dequeue()  # 30
    q.dequeue()  # Queue Underflow message
    print("Is queue empty now?", q.is_empty())  # True