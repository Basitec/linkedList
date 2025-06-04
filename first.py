numbers = [10,15,12,34,99]


i = 0
print("All the numbers in the array are: ")
while i < len(numbers):
    print(numbers[i])
    i+=1
    
    
class linkedListNode:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode
        
        
        
    
class linkedList:
    def __init__(self,head=None):
        self.head=head
        
    def insert(self,value ):
        node = linkedListNode(value)
        if self.head is  None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode=node
                break
            currentNode=currentNode.nextNode
            
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(f'"{currentNode.value}" -> ', end="")
            currentNode = currentNode.nextNode
        print("None")
        
        
ll = linkedList()
ll.printLinkedList()
ll.insert("2")
ll.printLinkedList()
ll.insert("3")
ll.printLinkedList()
ll.insert("4")
ll.printLinkedList()
        
# "3" -> "7" -> "10"
# node1 = linkedListNode("3")
# node2 = linkedListNode("7")
# node3 = linkedListNode("10")
# node1.nextNode = node2
# node2.nextNode = node3
# print(linkedListNode)
# currentNode = node1
# while currentNode is not None:
#     print(f'"{currentNode.value}" -> ', end="")
#     currentNode = currentNode.nextNode

# print("None") 

# while True:
#     # print(f"{currentNode.value} ->")
#     print(f'"{currentNode.value}" -> ', end="")
#     # print currentNode.value,"->"
#     if currentNode.nextNode is None:
#         print("None")
#         break
#     currentNode = currentNode.nextNode