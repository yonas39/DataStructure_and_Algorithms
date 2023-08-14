class BST:
  """ 
  Defines a Binary Search Tree (BST) node.
  """
  def __init__(self, value):
      """
      Initializes a BST node.
      
      Parameters:
      - value: The value stored at the node.
      """
      self.value = value
      self.right = None
      self.left  = None

def validateBst(tree):
  """
  Validates if a binary tree is a BST.
  
  Parameters:
    - tree: The root of the binary tree.
  
  Returns:
    - True if the tree is a BST, otherwise False.
  """
  def helper(tree, minValue, maxValue):
    """
    Recursive helper function to validate a subtree.
    
    Parameters:
    - tree: The root of the subtree.
    - minValue: The minimum allowed value for this subtree.
    - maxValue: The maximum allowed value for this subtree.
    
    Returns:
    - True if the subtree is a BST, otherwise False.
    """
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False

    # Validate left subtree with updated constraints.
    left_is_valid = helper(tree.left, minValue, tree.value)
    
    # Validate right subtree with updated constraints.
    right_is_valid = helper(tree.right, tree.value, maxValue)
    
    return left_is_valid and right_is_valid

  # Start the validation with initial constraints of negative and positive infinity.
  return helper(tree, float('-inf'), float('inf'))


