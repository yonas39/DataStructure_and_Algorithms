
def transpose(matrix):
  """
  :type matrix: List[List[int]]
  :rtype: List[List[int]]
  """
  out= []
  for col in range(len(matrix[0])):
      temp = []
      for row in range(len(matrix)):
          temp.append(matrix[row][col])
      out.append(temp)
  return out
