class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Update the matrix with the shortest distances from nearest 0 cells using BFS.
        
        :param mat: A 2D matrix containing 0s and 1s.
        :return: A matrix with shortest distances from nearest 0 cells.
        """
        row = len(mat)
        col = len(mat[0])
        result = [[float('inf')] * col for _ in range(row)]  # Initialize result matrix
        
        agenda = []
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    agenda.append((r, c))
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while agenda:
            rw, cl = agenda.pop(0)  # Dequeue a cell from the front of the queue
            
            # Explore neighbors
            for dr, dc in directions:
                nr = rw + dr
                nc = cl + dc
                
                if 0 <= nr < row and 0 <= nc < col:
                    new_distance = result[rw][cl] + 1
                    
                    if new_distance < result[nr][nc]:
                        agenda.append((nr, nc))
                        result[nr][nc] = new_distance
        
        return result
