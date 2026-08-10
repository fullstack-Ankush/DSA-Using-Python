# implementing singly linked list
#solution 1
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

#solution 2
class SLL:
    def __init__(self,start=None):
        self.start = start

    #solution3

    def is_empty(self):
       return  self.start == None
    
    # solution 4

    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n

    # solution 5
    def insert_at_last(self,data):
        n = Node(data,None)
        if not self.is_empty():
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    # SOLUTION 6

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None

    # solution 7 

    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n


    # solution 8
    def print_list(self):
        temp = self.start
        while(temp!=None):
            print(temp.item,end=' ')
            temp = temp.next

    # solution 9
    def delete_first(self):
        if self.start != None:
            self.start = self.start.next

    # solution 10

    def delete_last(self):
        if self.start == None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while(temp.next.next is not None):
                temp = temp.next
            temp.next = None



    # solution 11

    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next == None and self.start.item == data:
            self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while(temp.next.item is not None):
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)
# solution 12

class SLLIterator:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data
    


# driver code

mylist = SLL() 
mylist.insert_at_start(20)
mylist.insert_at_last(50)
mylist.insert_at_last(60)
mylist.insert_at_last(70)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
print()
mylist.delete_item(50)
for x in mylist:
    print(x,end=' ')
# mylist.print_list()
print()
