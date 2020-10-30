#reverse and compare
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
def reverse(node):
    if node.next==None:return node
    L=None
    p=node
    while p!=None:
        new=Node(p.data)
        new.next=L
        L=new
        p=p.next
    return L

def show(node):
    p=node
    while p!=None:
        print(p.data,end=',')
        p=p.next

def is_equal(node1,node2):
    p1=node1
    p2=node2
    while p1!=None and p2!=None:
        if p1.data!=p2.data:return False
        p2=p2.next
        p1=p1.next
    if p1!=None or p2!=None:
        return False
    return True
        
def is_palindrome(node):
    return is_equal(node,reverse(node))

root=Node(1,Node(2,Node(3,Node(2,Node(1)))))
root2=Node(1,Node(2,Node(3)))
print(is_palindrome(root))
print(is_palindrome(root2))
