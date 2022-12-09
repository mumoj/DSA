class MyLinkedList:

    class Node:
        def __init__(self, next, value: int) -> None:
            self.next = next
            self.value: int = value
            

    def __init__(self) -> int:
        self.head = None
        self.length = 0
       
    def get(self, index: int) -> int:

        curr_node = self.head
        if index < 0 or index >= self.length: 
            return -1

        count = 0
        while (curr_node.next != None):
            if count == index:
                return curr_node.value
            curr_node = curr_node.next
            count += 1

        return curr_node.value

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(next=self.head, value=val)
        self.head = new_node
        self.length +=1

    def addAtTail(self, val: int) -> None:
        curr_node = self.head

        if curr_node == None:
            self.addAtHead(val)
            return

        while(curr_node.next != None):
            curr_node = curr_node.next
        curr_node.next = self.Node(next=None, value=val)
        self.length +=1
        
    def addAtIndex(self, index: int, val: int) -> None:
        curr_node = self.head

        if index > self.length:
            return

        if index == 0 :
            self.addAtHead(val)

        elif index == self.length:
            self.addAtTail(val)

        else:
            count: int = 0
            prev_node = None
            while(curr_node.next != None):
                if index == count:
                    new_node = self.Node(next=curr_node, value=val)
                    if prev_node: prev_node.next = new_node
                    self.length +=1
                    return

                prev_node = curr_node
                curr_node = curr_node.next
                count += 1

            if index == count:
                new_node = self.Node(next=curr_node, value=val)
                prev_node.next = new_node
                new_node.next = curr_node
                self.length +=1

    def deleteAtIndex(self, index: int) -> None:
        curr_node = self.head

        if index == 0:
            if curr_node: self.head = curr_node.next
            del curr_node
            self.length -=1
            return

        count: int = 0
        prev_node = None
        while (curr_node.next != None):
            if index == count:
                next_node = curr_node.next
                if prev_node: prev_node.next = next_node
                del curr_node
                self.length -= 1
                return

            prev_node = curr_node
            curr_node = curr_node.next
            count += 1

        if index == self.length-1:
            prev_node.next = None
            del curr_node
            self.length -= 1

    
    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)