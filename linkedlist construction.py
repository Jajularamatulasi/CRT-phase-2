
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj1=node(10)
obj2=node(20)
obj3=node(30)
obj4=node(40)
obj5=node(50)

obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5

currentnode=obj1
while currentnode!=None:
    print(currentnode.data,end="-->")
    currentnode=currentnode.next



