class LinkedList:

    class Node:
        def __init__(self, next, index: int, value: int) -> None:
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
            self.head = self.Node(next=None, index=0, value=val)
            self.indexes.append(0)

        else:
            n = self.Node()



        
        





        




            

        else:
            return -1









    
        
    


        
            