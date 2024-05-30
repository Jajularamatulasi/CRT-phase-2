class Node:
    def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None



def printInorder(root):
    if root==None:
        return
    printInorder(root.left)
    print(root.data,end='  , ')
   
    printInorder(root.right)

    
    
obj1=Node(12)
obj2= Node(5)
obj3=Node(8)
obj4=Node(-1)
obj5=Node(2)
obj6=Node(89)


obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6


printInorder(obj1)
print()

