


class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None 


def buildList() :
    data = int(input('Enter head data : '))
    if data == -1 :
        return None 
    head = Node(data)
    temp = head
    while True :
        data = int(input('Enter node data : '))
        if data == -1 :
            break
        newNode = Node(data)    # Create a newNode 
        temp.next = newNode # Connect current Node with previous
        temp = newNode 
    return head
def printList(head) :
    while head is not None :
        print(head.data, end = ' ')
        head = head.next 

# Printing Address of node before calling rest of LL and after calling rest of LL 
def printList1(head) :
    if head is None :
        return 
    print('Data of Node : ',head.data,  'address of current node : ', id(head))
    printList1(head.next)
    print('Data of Node : ',head.data,  'address of current node : ', id(head))


head = buildList()
printList(head)









'''
class Student :
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
        print('Inside init : ', id(self))
    def printStudent(self) :
        print('Name : ', self.name ,'Roll Number : ', self.rollNumber)

s1 = Student('abc', 10)
print('Address of s1 : ', id(s1))
s2 = Student('def', 20)
print('Address of s2 : ', id(s2))

'''

'''
n = int(input('Enter n : '))
size = (2 * n) - 1
for i in range(size) :
    for j in range(size) :
        top, left, down, right = i, j, size - 1 - i, size - 1 - j
        k = min(top, left, down, right)
        print(n - k, end = ' ')
    print()
'''
