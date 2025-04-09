class Node:
    """Node class for linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked list implementation"""
    def __init__(self):
        self.head = None

    def display(self):
        """Display the linked list contents"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, target_data, new_data):
        """Insert a new node after a specific node"""
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Target node {target_data} not found")

    def delete_node(self, data):
        """Delete a node with given data"""
        if self.head is None:
            print("List is empty")
            return

        # If head node needs to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"Node with data {data} not found")


# Example usage
if __name__ == "__main__":
    ll = LinkedList()

    # Insert operations
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_after(10, 15)

    print("Linked List:")
    ll.display()  # 5 -> 10 -> 15 -> 20 -> None

    # Delete operations
    ll.delete_node(15)
    print("After deleting 15:")
    ll.display()  # 5 -> 10 -> 20 -> None

    ll.delete_node(5)
    print("After deleting 5:")
    ll.display()  # 10 -> 20 -> None

    ll.delete_node(99)  # Will print "Node with data 99 not found"