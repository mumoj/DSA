class LinkedList:

    class Node:
        def __init__(self, next, value: int) -> None:
            self.next = next
            self.value: int = value
            

    def __init__(self) -> int:
        self.head = None
       
    def get(self, index: int) -> int:

        n = self.head

        if n == None:
            return -1

        elif index == 0 :
            return n.value 

        count = 0
        while (n.next != None):
            n = n.next
            count += 1
            if count == index:
                return n.value
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = self.Node(next=None, value=val)
   
        else:
            new_node = self.Node(next=self.head, value=val)
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        curr_node = self.head

        if curr_node == None:
            self.head = self.Node(next=None, value=val)

        while(curr_node.next != None):
            curr_node = curr_node.next

        curr_node.next = self.Node(next=None, value=val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr_node = self.head

        if curr_node:
            if curr_node.next == None and index == 0 :
                new_node = self.Node(next=curr_node, value=val)
                self.head = new_node

            count: int = 0
            prev_node = None 
            while(curr_node.next != None):
                if index == count:
                    new_node = self.Node(next=curr_node, value=val)
                    if prev_node: prev_node.next = new_node
                    else: self.head = new_node

                prev_node = curr_node
                curr_node = curr_node.next
                count += 1

            if index == count+1:
                new_node = self.Node(next=None,value=val)
                curr_node.next = new_node
        else:
            if index==0:
                self.head = self.Node(next=None,value=val)

        def deleteAtIndex(self, index: int, val: int) -> None:
            curr_node = self.head

            if curr_node:
                count = 0

                if curr_node.next == None and index == 0:
                    del self.head

                count: int = 0
                prev_node = None
                while (curr_node.next != None):
                    if index == count:
                        next_node = curr_node.next
                        if prev_node: prev_node.next = next_node
                        del curr_node
                        break

                    prev_node = curr_node
                    curr_node = curr_node.next
                    count += 1

                if count == index:
                    prev_node.next = None
                    del curr_node

n = LinkedList()
print(n)