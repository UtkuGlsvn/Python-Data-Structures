# @Author: utkuglsvn <utkuglsvn>
# @Date:   2019-04-19T13:43:04+03:00
# @Last modified by:   utkuglsvn
# @Last modified time: 2019-04-19T14:01:19+03:00

#python stack = list
class Stack:
    def __init__(self):
        self.stack=list()
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print("Stack is empty")
    def printStack(self):
        print(self.stack)
if __name__=="__main__":
    stack=Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    stack.push(20)
    print("Print Stack")
    stack.printStack()
    print(50*'-')
    print("Pop Stack")
    stack.pop()
    stack.pop()
    stack.printStack()
