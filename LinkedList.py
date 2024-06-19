# =============================== Linked List 
#  linear data structure who have collection of nodes that are linked with each other.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:  # If the list is empty
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # Insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location >= self.length():  # Insert at the end
                self.tail.next = newNode
                self.tail = newNode
            else:  # Insert at the given location
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    
    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

# ======================================> search a value in linked list
    # def searchSSL(self, nodeValue):
    #     if self.head is None:
    #         return "The list does not exist"
    #     else:
    #         node = self.head
    #         while node is not None:
    #             if node.value == nodeValue:
    #                 return node.value
    #             node = node.next
    #         return "The value does not exist "

# ===============================================> deletion in linked list



# singleLinkedList = SLinkedList()  # Create an instance of the SLinkedList class
# singleLinkedList.insertSLL(1, 0)  # Insert value 1 at the beginning of the list
# singleLinkedList.insertSLL(2, 1)  # Insert value 2 at the end of the list
# singleLinkedList.insertSLL(3, 2)  # Insert value 3 at the end of the list
# singleLinkedList.insertSLL(4, 1)  # Insert value 4 at position 1

# print(singleLinkedList.searchSSL(2))

# print([node.value for node in singleLinkedList])  # Output the list values
