class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def buildLevelOrder(array, root, i):
    if i < len(array):
        temp = Node(array[i])
        root = temp
        root.left = buildLevelOrder(array, root.left, 2 * i + 1)
        root.right = buildLevelOrder(array, root.right, 2 * i + 2)

    return root

def buildBST(array, root):
    if not array:
        return None

    mid = len(array) // 2
    root = Node(array[mid])
    root.left = buildBST(array[:mid], root.left)
    root.right = buildBST(array[mid + 1:], root.right)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data)
        inOrder(root.left)
        inOrder(root.right)

def postOrder(root):
    if root:
        inOrder(root.left)
        inOrder(root.right)
        print(root.data)

# Print BST in descending order, by starting from the right instead of left
def inDescOrder(root):
    if root:
        inDescOrder(root.right)
        print(root.data)
        inDescOrder(root.left)

array = [1, 2, 3, 4, 5, 6, 7]
print(f'Binary tree from array: {str(array)}')
root = buildLevelOrder(array, Node(None), 0)
print('Level order')
inOrder(root)

root = buildBST(array, Node(None))
print('BST')
inDescOrder(root)
