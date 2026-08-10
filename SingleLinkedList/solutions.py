# solution 1

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

# solution 2

class SLL:
    def __init__(self,start=None):
        self.start = start


    # solution 3

    def is_empty(self):
        if self.start == None:
            return True

    # solution 4

    def insert_at_begin(self,data):
        n = Node(data,self.start)
        self.start = n

    # solution 5

    def insert_at_last(self,data):
        n = Node(data,None)
        if self.is_empty is None :
            self.start = n
        else:   
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = n    

