class Solution(object):
    def findMin(self, array):
        """
        :type nums: List[int]
        :rtype: int

        Steps:
        # The principle of Binary search can be implemented to solve this problem. 
        1. Initialize low, high, min_val, 0 and len(array)-1, large integer respectively. 
        2. Enter a while loop that has a condition of low<=high. if low > high it terminates. 
        3. initialize a mid as (low+high)//2
        4. if the array[mid] >= array[0] explore the right side by increasing the low pointer to m+1 update the min_val as min(min_val, array[mid])
        5. if the array[mid]< array[0] explore the left side update the min_val as min(min_val, array[mid])
        6. when the loop is complete return mid_val

        """
        low, high = 0, len(array)-1
        min_val = float('inf')
        
        while low <= high:
            mid = (low+high)//2
            print(mid)
            if array[0] < array[-1]:
                min_val= min(min_val, array[low])
                return min_val
            elif array[mid]>=array[0]:
                low = mid+1
                min_val= min(min_val, array[mid])
            else:
                min_val = min(min_val, array[mid])
                high = mid-1
        return min_val
