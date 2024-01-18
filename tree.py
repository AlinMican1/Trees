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

    # Delete Node
    def deleteNode(self, root, key):
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted found

            # Case 1: Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 2: Node with two children
            # Find the inorder successor (smallest node in the right subtree)
            successor = self.find_min(root.right)

            # Copy the inorder successor's value to this node
            root.val = successor.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def find_min(self, node):
        # Helper method to find the minimum value node in a BST
        current = node
        while current.left:
            current = current.left
        return current
        # def dfs(root):
        #     if not root:
        #         return
        #     if root.val == node:
        #         root.val = None
        #     return dfs(root.left), dfs(root.right)

        # return dfs(self)

    # This is to print the tree INORDER
    def InOrder(self):
        if self.left:
            self.left.InOrder()
        if self.val is not None:
            print(self.val)
        if self.right:
            self.right.InOrder()

    # PreOrder print
    def PreOrder(self):
        if self.val is not None:
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
        if self.val is not None:
            print(self.val)
