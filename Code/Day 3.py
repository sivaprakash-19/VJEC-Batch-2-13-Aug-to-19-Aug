


# Queues from Collections
from collections import deque 

queue = deque() 
for i in range(5) :
    queue.append(i + 2)

print(queue)
print('Top most element : ', queue[0])

i = 0
while queue :
    print(i, ' element : ' , queue.popleft())
    i += 1





'''
# Queue - FIFO
class Queue : 
    def __init__(self):
        self.queue = [] 

    def enqueue(self, element) : 
        self.queue.append(element)

    def dequeue(self) :
        if len(self.queue) == 0 :
            return 'Queue is Empty'  
        value = self.queue[0] 
        self.queue = self.queue[1 : ]
        return value 

    def top(self) :
        if len(self.queue) == 0 :
            return 'Queue is Empty'
        return self.queue[0] 
    
    def isEmpty(self) :
        return len(self.queue) == 0
'''

'''
class Node :
    def __init__(self, data):
        self.data = data 
        self.next = None 
# Stack is a DS, which follows LIFO order - implemented using Linked List
class Stack : 
    def __init__(self):
        self.head = None 
    # Push elements into stack 
    def push(self, element) :
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode
    # Pop elements into stack
    def pop(self) :
        if self.head is None :
            return 'Stack is Empty!'
        value = self.head.data 
        self.head = self.head.next
        return value 
    # Returns the top most element from  stack
    def top(self) :
        if self.head is None :
            return 'Stack is Empty!'
        return self.head.data
    # Returns true if stack is empty, otherwise false 
    def isEmpty(self) :
        return self.head is None 

'''



'''
# Stack is a DS, which follows LIFO order - implemented using LIST
class Stack : 
    def __init__(self):
        self.stack = []     # Creating a stack
    # Push elements into stack 
    def push(self, element) :
        self.stack.append(element)
    # Removes the last element in stack
    def pop(self) :
        if self.isEmpty() :
            return 'Stack is Empty!'
        value = self.stack.pop() 
        return value
    # Returns the top element in stack
    def top(self) :
        if self.isEmpty() :
            return 'Stack is Empty!'
        return self.stack[-1]
    # Returns true if stack is empty, false otherwise
    def isEmpty(self) :
        return len(self.stack) == 0
'''


# st1 = Stack() 
# print('Topmost element in stack : ' , st1.top())
# for i in range(6) :
#     st1.push(i + 1)
# print('Topmost element in stack : ' , st1.top())

# while not st1.isEmpty() :
#     print(st1.pop(), end = ' ')



'''
# Using a list as a stack
stack = [] 

# Adding elements into stack
for i in range(5) :
    stack.append(i)

print(stack)

# Removing elements, till stack is getting empty
while stack :
    print(stack.pop())
'''