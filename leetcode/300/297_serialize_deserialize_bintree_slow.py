import queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        q = queue.Queue()
        l = []
        l.append(str(root.val))
        q.put(root.left)
        q.put(root.right)
        
        
        while not q.empty():
            n = q.get()
            if n == None:
                l.append("_")
                continue
            l.append(str(n.val))
            q.put(n.left)
            q.put(n.right)
        return " ".join(l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        slist = data.split(" ")
        nlist = []
        nlist.append(TreeNode(int(slist[0])))
        
        j, l = 0, 1
        for i in range(1,len(slist)):
            if slist[i] != '_':
                t = TreeNode(int(slist[i]))
                nlist.append(t)
                if l:
                    nlist[j].left = t
                    l = 0
                else:
                    nlist[j].right = t
                    l = 1
                    j += 1
            else:
                if l == 0:
                    j += 1
                    l = 1
                else:
                    l = 0
        return nlist[0]
                    
                
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))