class TreeNode:
	def __init__(self,val,left=None,right=None):  # 二叉树节点
		self.val = val
		self.left = left
		self.right = right


class BinaryTree:  # 二叉树
	def __init__(self,root=None):  
		self.root = root

	def preScan(self,re_list,node):  # 先序遍历
		if node != None:
			re_list.append(node.val)
			self.preScan(re_list,node.left)
			self.preScan(re_list,node.right)
		return re_list

	def midScan(self,re_list,node):  # 中序遍历
		if node != None:
			self.midScan(re_list,node.left)
			re_list.append(node.val)
			self.midScan(re_list,node.right)
		return re_list

	def postScan(self,re_list,node):  # 后序遍历
		if node != None:
			self.postScan(re_list,node.left)
			self.postScan(re_list,node.right)
			re_list.append(node.val)
		return re_list


root = TreeNode(50)
root.left = TreeNode(20,left=TreeNode(15),right=TreeNode(30,right=TreeNode(35)))
root.right = TreeNode(60,left=TreeNode(55),right=TreeNode(70,left=TreeNode(65),right=TreeNode(80)))

bTree = BinaryTree(root)

list1 = bTree.midScan([],bTree.root)

print(list1)