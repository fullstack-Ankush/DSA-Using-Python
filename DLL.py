# DOUBLY LINKED LIST CODE : )

#solution 1
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev= prev
        self.item = item
        self.next = next

# solution 2 

class DLL:
    def __init__(self,start=None):
        self.start= start

    #solution 3
    def is_empty(self):
        return self.start==None

    # solution 4

    def insert_at_start(self,data):
        n =Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev =n
        self.start =n

    # solution 5

    def insert_at_end(self,data):
        temp=self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next

        n=Node(temp,data,None)
        if temp ==None:
            self.start = n
        else:
            temp.next =n

    # solution 6
    def search(self,data):
        temp = self.start
        while(temp != None):
            if temp.item == data:
                return temp
            temp=temp.next
        return None

    # solution 7
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    # solution 8
    def print_list(self):
        temp =self.start
        while(temp is not None):
            print(temp.item,end=' ')
            temp=temp.next


    # solution 9
    def __iter__(self):
        return DLLiterator(self.start)


    # solution 10
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    # solution 11

    def delete_last(self):
        if self.start == None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next=None

    # solution 12


    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp=temp.next


class DLLiterator:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_end(20)
mylist.insert_after(mylist.search(10),15)
for x in mylist:
    print(x,end=" ")
print()