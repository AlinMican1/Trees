from tree import TreeNode

root = TreeNode(4)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(3)

# root.insert(2)
# root.insert(4)
# root.insert(10)
# root.insert(0)
# root.insert(7)


root1 = TreeNode(3)
root1.insert(5)
root1.insert(6)
root1.insert(2)
root1.insert(4)
root1.insert(10)
root1.insert(0)
root1.insert(7)

root.deleteNode(6)
root.InOrder()
# print(root.isSameTree(root1))

# print(root.getLeafs())
