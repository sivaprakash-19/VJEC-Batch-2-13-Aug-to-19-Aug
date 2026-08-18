class Node :
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

def buildTree(message) :
    data = int(input(message))
    if data == -1 :
        return None
    root = Node(data) 
    root.left = buildTree('Enter left of ' + str(data) + ' : ')
    root.right = buildTree('Enter right of ' + str(data) + ' : ')
    return root

def printTree(root) :
    if root is None :
        return 
    print(root.data , end = ' : ')
    if root.left :
        print('L', root.left.data , end = ' ')
    if root.right :
        print('R', root.right.data , end = ' ')
    print()
    printTree(root.left)
    printTree(root.right)

root = buildTree('Enter root data : ')
printTree(root)