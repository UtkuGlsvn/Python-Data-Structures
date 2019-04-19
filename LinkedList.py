# @Author: utkuglsvn
# @Date:   2019-04-18T14:59:31+03:00
# @Last modified by:   glsvn
# @Last modified time: 2019-04-19T12:56:47+03:00

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None

    def insert(self,value):
        if self.start==None:
            self.start=Node(value)

        current=self.start
        while current.next is not None:
            current=current.next

        current.next=Node(value)

    def printList(self):
        if self.start==None:
            print("List empty:")
        current=self.start
        while current.next is not None:
            current=current.next
            print("List:"+str(current.value))

    def delete(self,n):
        current=self.start

        if (current is not None):
            if (current.value == n):
                self.start = current.next
                current = None
                return

        while current is not None:
            if(current.value==n):
                break
            prev = current
            current=current.next

        if(current == None):
			return

        prev.next = current.next




if __name__=="__main__":
    linkedlist = LinkedList()
    #insert list
    linkedlist.insert(10)
    linkedlist.insert(15)
    linkedlist.insert(20)
    linkedlist.insert(21)
    print("Create List")
    linkedlist.printList()
    print("Delete Value:20")
    #delete list
    linkedlist.delete(20)
    #print list
    linkedlist.printList()
