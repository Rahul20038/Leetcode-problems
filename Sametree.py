#same tree leetcode problem to check the tress are same 
class Treenode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(p: Treenode, q: Treenode ) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
root1 = Treenode(1)
root1.left = Treenode(2)
root1.right = Treenode(3)

root2 = Treenode(1)
root2.left = Treenode(2)
root2.right = Treenode(3)
print(isSameTree(root1, root2))