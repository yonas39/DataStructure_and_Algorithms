# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    # Recursive method 
    def isSameTree(self, p, q):
        """
        Determine if two binary trees are identical in structure and value.

        Given the roots of two binary trees 'p' and 'q', this method checks 
        if they are structurally identical and have the same node values.

        Args:
        - p (TreeNode): Root node of the first binary tree.
        - q (TreeNode): Root node of the second binary tree.

        Returns:
        - bool: True if both trees are identical, False otherwise.
        """
        
        # Base cases: if both nodes are None, trees are still identical up to this point.
        if not p and not q:
            return True
        
        # If one of the nodes is None and the other isn't, trees are different.
        if not p or not q:
            return False
        
        # Nodes have different values, trees are different.
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees for both nodes.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # Iterative Method
    def isSameTree_iter(self, p, q):
        """
        Determine if two binary trees are identical in structure and value using an iterative approach.

        Args:
        - p (TreeNode): Root node of the first binary tree.
        - q (TreeNode): Root node of the second binary tree.

        Returns:
        - bool: True if both trees are identical, False otherwise.
        """
        
        # Base case: If both trees are empty, they are the same.
        if not q and not p:
            return True

        # Initialize two stacks for each tree's nodes.
        stack_q, stack_p = [q], [p]

        # Continue until both stacks are empty.
        while stack_q or stack_p:
            # Pop nodes from the stacks. If a stack is empty, assign None.
            node_q = stack_q.pop() if stack_q else None
            node_p = stack_p.pop() if stack_p else None
            
            # If one node exists and the other doesn't, the trees aren't identical.
            if not node_q and node_p or node_q and not node_p:
                return False
            
            # If both nodes exist but have different values, the trees aren't identical.
            if node_q and node_p and node_q.val != node_p.val:
                return False
            
            # If both nodes exist, push their children onto the stacks if they also exist.
            if node_q and node_p:
                # If both nodes have right children, push them. Otherwise, check for mismatch.
                if node_q.right and node_p.right:
                    stack_q.append(node_q.right)
                    stack_p.append(node_p.right)
                elif (not node_q.right and node_p.right) or (node_q.right and not node_p.right):
                    return False
                
                # If both nodes have left children, push them. Otherwise, check for mismatch.
                if node_q.left and node_p.left:
                    stack_q.append(node_q.left)
                    stack_p.append(node_p.left)
                elif (not node_q.left and node_p.left) or (node_q.left and not node_p.left):
                    return False

        # If both stacks are empty at the same time, the trees are identical.
        return True
