class Solution:
    def spiralOrder(self, matrix):
        """
        Traverse a 2D matrix in a spiral order.

        :param matrix: A 2D matrix to be traversed.
        :return: A list of elements in spiral order.
        """
        result = []
        sr, sc = 0, 0
        er, ec = len(matrix) - 1, len(matrix[0]) - 1
        
        while sr <= er and sc <= ec:
            # Traverse from left to right
            for col in range(sr, ec + 1):
                result.append(matrix[sr][col])
            
            # Traverse from top to bottom
            for row in range(sr + 1, er + 1):
                result.append(matrix[row][ec])

            # Traverse from right to left (if applicable)
            for col in reversed(range(sc, ec)):
                if sr == er:
                    break
                result.append(matrix[er][col])
            
            # Traverse from bottom to top (if applicable)
            for row in reversed(range(sr + 1, er)):
                if sc == ec:
                    break
                result.append(matrix[row][sc])
            
            # Update pointers for the next iteration
            sr += 1
            sc += 1
            ec -= 1
            er -= 1
        
        return result
