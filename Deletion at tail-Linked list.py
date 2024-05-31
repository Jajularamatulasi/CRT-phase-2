class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
def printLinkedList(head):
    currentNode=head
    while currentNode!=None:
        print(currentNode.data,end="--->")
        currentNode=currentNode.next
    print()
def insertAttail(head,ele):
    temp=Node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
def deleteTailNode(head):
    if head==None or head.next==None:
        return None
    previous=None
    currentNode=head
    while currentNode.next!=None:
        previous=currentNode
        currentNode=currentNode.next
    previous.next=None
    return head
nums=[10,20,30,40,50]
head=None
for ele in nums:
    head=deleteTailNode(tail)
print("Final linked list is:")
printLinkedList(head)
