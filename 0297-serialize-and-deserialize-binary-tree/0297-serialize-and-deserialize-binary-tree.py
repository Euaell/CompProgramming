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
        if not root:
            return ""
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        tmp = str(root.val) + "(" + left + ")" + "(" + right + ")"
        return tmp

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        i = 0
        while i < len(data) and data[i] != "(":
            i += 1
        root = TreeNode(int(data[:i]))

        # find the left subtree
        left = self.findClosing(data, i)
        root.left = self.deserialize(data[i+1:left])

        # find the right subtree
        right = self.findClosing(data, left+1)
        root.right = self.deserialize(data[left+2:right])

        return root
        
    
    def findClosing(self, data, i):
        count = 0
        while i < len(data):
            if data[i] == "(":
                count += 1
            elif data[i] == ")":
                count -= 1
            if count == 0:
                return i
            i += 1

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))