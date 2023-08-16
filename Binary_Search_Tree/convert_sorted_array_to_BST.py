# Definition for a binary tree node.
class TreeNode(object):
    """
    A class definition for a binary tree node. 

    Attributes:
    - val (int): The value of the node.
    - left (TreeNode, optional): Left child node. Defaults to None.
    - right (TreeNode, optional): Right child node. Defaults to None.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Convert a sorted array to a balanced binary search tree (BST).

        The middle element of the array becomes the root, and this process is
        recursively applied to the left and right sub-arrays to construct the
        left and right subtrees, ensuring a height-balanced BST.

        Args:
        - nums (List[int]): A sorted integer array.

        Returns:
        - TreeNode: Root node of the constructed BST.
        """
        
        # Base condition: if the array is empty, return None
        if not nums:
            return None
        
        # Find the middle element to be the root
        mid = len(nums) // 2
        
        # Create the root node with the middle value
        root = TreeNode(nums[mid])
        
        # Construct the left subtree using the left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Construct the right subtree using the right half of the array
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
