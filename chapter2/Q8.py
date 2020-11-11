class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def loop_detection(node):
    a,b=node,node
    while b!=None and b.next!=None:
        a=a.next
        b=b.next.next
        if a==b:break
    if b==None or b.next==None:return
    a=node
    while a!=b:
        a=a.next
        b=b.next
    return a
    
#n3 is the loop starting point in the linked list
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n3
loop_start=loop_detection(n1)
print(loop_start.data)
