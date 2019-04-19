# @Author: utkuglsvn <utkuglsvn>
# @Date:   2019-04-19T13:11:10+03:00
# @Last modified by:   utkuglsvn
# @Last modified time: 2019-04-19T13:54:55+03:00

class Queue:
    def __init__(self):
        self.queue=list()
        self.first=None
        self.last=None

    def enqueue(self,value):
        if self.first==None or self.last==None:
            self.first=0
            self.last=0
        self.queue.insert(self.last,value)
        self.last=self.last+1

    def popqueue(self):
        self.queue.pop(self.first)

    def printQueue(self):
        for i in range(0,len(self.queue)):
            print(self.queue[i])

    def valueCheckQueue(self,value):
        for i in range(0,len(self.queue)):
            if value == self.queue[i]:
                print("The value is already there")
                break
            else:
                print("The value is not already there")
                break


if __name__=="__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(105)
    queue.enqueue('a')
    print("Print queue")
    queue.printQueue()
    print(50*'-')
    print("pop queue")
    queue.popqueue()
    queue.printQueue()
    print(50*'-')
    print("Check Value queue")
    queue.valueCheckQueue("b")
