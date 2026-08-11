# solution 1
class Node:
    def __init__(self,prev,data,next):
        self.item = data
        self.next = next
        self.prev = prev

# solution 2
class DLL:
    def __init__(self,start=None):
        self.start = start


    # solution 3

    def isempty(self):
        if (self.start == None):
            return True

        
    # solution 4

    def insert_at_start(self,data):
        if (not self.isempty()):
          n = Node(None,data,self.start)
          self.start.prev = n
          self.start = n
        else:
            n = Node(None,data,None)
            self.start = n


    # solution 5


    def insert_at_end(self,data):
        temp = self.start

        if(self.isempty()):
            n = Node(None,data,None)
            self.start = n
        else:
            while(temp.next != None):

                if(temp.next == None):
                    n = Node(temp.next,data,None)
                    temp.next = n
                temp =temp.next 


    # solution 6

    def search(self,data):
        temp = self.start
        while(temp!=None):
            if temp.item == data:
                return temp

        return None
