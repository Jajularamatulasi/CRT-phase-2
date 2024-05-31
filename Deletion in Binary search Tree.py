class TreeNode:
    def __init__(self, data):
        self.val = data 
        self.left = None 
        self.right = None
 
def printInorder(root):
    if root == None:
        return 
    printInorder(root.left)
    print(root.val, end = ", ")
    printInorder(root.right)
 
 
def deleteNodeFromBST(root, val):
    if root == None:
        return None 
    elif root.val > val:
        root.left = deleteNodeFromBST(root.left, val)
    elif root.val < val:
        root.right = deleteNodeFromBST(root.right, val)
    else:
 
        if root.left == None and root.right == None:
            return None
 
        if root.left == None:
            return root.right 
        elif root.right == None:
            return root.left
  
        curr = root.right 
        while curr.left != None:
            curr = curr.left 
 
        root.val = curr.val 
        root.right = deleteNodeFromBST(root.right, curr.val)
    return root 
 
nums = [10, 8, 12, 5, 23, 20, 43, 23, 11, 7]
root = None
for ele in nums:
    root = deleteNodeFromBST(root, 20)
printInorder(root)
