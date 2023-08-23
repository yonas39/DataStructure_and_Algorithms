class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Check if the given matrix is a Toeplitz matrix.

        A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

        :param matrix: A 2D matrix.
        :return: True if matrix is Toeplitz, False otherwise.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        direction = [(1, 1)]  # Direction of the diagonal (down and right)
        
        # Loop through each cell in the matrix
        for row in range(rows):
            for col in range(cols):
                nr = row + direction[0][0]  # Calculate the next row index
                nc = col + direction[0][1]  # Calculate the next column index
                
                # Check if the next cell is within matrix boundaries
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Compare the current cell with the next cell along the diagonal
                    if matrix[row][col] != matrix[nr][nc]:
                        return False  # Not a Toeplitz matrix
                    
        return True  # Matrix is Toeplitz
