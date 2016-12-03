class Stack:
    def __init__(self):
        self.size = 100
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        last = len(self.data) - 1
        self.data.pop(last)

    def pop1(self):
        last = len(self.data) - 1
        del self.data[last]

    def show_all(self):
        print(self.data)

    # See the last item
    def peek(self):
        last = len(self.data) - 1
        return self.data[last]

if __name__ == '__main__':
    stack = Stack()
    stack.push('1')
    stack.push('a')
    stack.push('4')
    stack.pop()
    stack.push('7')
    stack.push('6')
    stack.show_all()
    stack.pop1()
    print("Peek: %s" % stack.peek())

