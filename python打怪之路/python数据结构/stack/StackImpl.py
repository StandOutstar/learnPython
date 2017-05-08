
# 2017-05-08 23:50:44
# 栈的实现


class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, content):
        if self.full():
            print('Stack is full')
        else:
            self.stack.append(content)
            print('append : ', content)
            self.top += 1

    def pull(self):
        if self.empty():
            print('stack is empty')
        else:
            print('pop : ', self.stack.pop())
            self.top -= 1

if __name__ == '__main__':
    s = Stack(7)
    print(s.empty())

    s.push('1')
    s.push('2')
    s.push('3')
    s.push('4')
    s.push('5')
    s.push('6')
    s.push('7')
    s.push('8')
    s.push('9')
    s.pull()
    s.pull()
    s.pull()
    s.pull()
    s.pull()
    s.pull()
    s.pull()
    s.pull()
    s.pull()


# 完成时间2017-05-09 00:14:34


