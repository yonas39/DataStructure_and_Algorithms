# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, value, left=None, right = None):
    self.val   = value
    self.left  = left
    self.right = right

class Solution(object):
    #  Recursive Method 
    def inorderTraversal(self, root):
      """
      Perform an inorder traversal of a binary tree.
      
      Given the root of a binary tree, this method returns a list of node 
      values in the order of an inorder traversal.
      
      Parameters:
      - root (TreeNode): The root node of the binary tree.
      
      Returns:
      - List[int]: A list of integers representing the node values in the order 
        of an inorder traversal.

      """
      if not root:
          return []
      out =[]
      out += self.inorderTraversal(root.left)
      out.append(root.val)
      out += self.inorderTraversal(root.right)
      return out

    # Iterative Method 
    def inorderTraversal_iter(self, root):
      """
      Perform an iterative inorder traversal of a binary tree.

      Given the root of a binary tree, this method returns a list of node 
      values in the order of an inorder traversal without using recursion.

      Args:
      - root (TreeNode): The root node of the binary tree.

      Returns:
      - List[int]: A list of integers representing the node values in the 
        order of an inorder traversal.
      """
      # Initialize an empty stack and result list.
      stack  = []
      result = []

      # Start from the root.
      curr = root

      # Continue traversal until all nodes are processed.
      while curr or stack :

        # Traverse to the leftmost node of the current subtree.
        while curr:
          stack.append(curr)
          curr = curr.left
        
         # Pop the current node from the stack and process its value.
        curr = stack.pop()
        result.append(curr.val)

        # Move to the right subtree of the current node.
        curr = curr.right

      # Return the result of the inorder traversal.
      return result 