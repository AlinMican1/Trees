class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        # This if statement checks if there is a root. self.val is the root

        if self.val:
            # This checks if the value is bigger than the root.
            if self.val > val:
                # This checks if the left value is empty
                if self.left is None:
                    # Add the value to the Treenode
                    self.left = TreeNode(val)
                else:
                    # Call recursion to move down the tree and add it.
                    self.left.insert(val)
            # Check if the value is less than
            elif self.val < val:
                # Check if the value is none
                if self.right is None:
                    # Add the value
                    self.right = TreeNode(val)
                # Otherwise recurse until an empty node is found
                else:
                    self.right.insert(val)
        else:
            self.val = val

    # Check to see if the trees are the same.
    def isSameTree(self, other_root):
        def dfs(root):
            if not root:
                return [None]
            return [root.val] + dfs(root.left) + dfs(root.right)

        return dfs(self) == dfs(other_root)

    def getLeafs(self):
        leafs = set()

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not root.left and not root.right:
                leafs.add(root.val)
            dfs(root.right)

        dfs(self)
        return "The leafs of the tree are: ", leafs

    def deleteNode(self, node):
        def dfs(root):
            if not root:
                return
            if root.val == node:
                root.val = 0
            return dfs(root.left), dfs(root.right)

        return dfs(self)

    # This is to print the tree INORDER
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.val)
        if self.right:
            self.right.InOrder()

    # PreOrder print
    def PreOrder(self):
        print(self.val)
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    # PostOrder print
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.val)
