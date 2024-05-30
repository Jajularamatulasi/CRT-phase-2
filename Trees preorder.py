class Node:
    def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None



def printPreorder(root):
    if root==None:
        return
    print(root.data,end='  , ')
    printPreorder(root.left)
    printPreorder(root.right)

    
    
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


printPreorder(obj1)
print()



    
