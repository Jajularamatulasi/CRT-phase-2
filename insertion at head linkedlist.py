class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLinkedList(head):
    currentNode=head
    while currentNode!=None:
        print(currentNode.data,end="-->")
        currentNode=currentNode.next
    print()
def insertAtTail(head,ele):
    temp=Node(ele)
    if head==None:
     return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
#Task-1
def insertAtHead(head,ele):
    temp=Node(ele)
    temp.next=head
    return temp

nums=[10,20,30,40,50,60,70,80,90,100]
head=None
for ele in nums:
    head=insertAtHead(head,ele)
print("Final Linked List is:")
printLinkedList(head)

