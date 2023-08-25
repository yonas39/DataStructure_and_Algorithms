def solution(picture):
    """
    This function takes a list of strings representing rows of a 'picture'
    and returns a new list where the 'picture' is framed by asterisks (*).
    
    For example:
    If picture = ["abc", "def"], the function will return ["*****", "*abc*", "*def*", "*****"].
    
    Parameters:
    - picture: A list of strings, where each string represents a row of the picture.
    
    Returns:
    - A list of strings, where the original picture is framed by asterisks.
    """
    
    # Determine the number of columns in the original picture
    col = len(picture[0])
    
    # Initialize the result list with the top row of asterisks
    result = ["*" * (col + 2)]
    
    # Loop through each row in the original picture
    # Add asterisks to the beginning and end of each row, then append it to 'result'
    for row in picture:
        result.append("*" + row + "*")
    
    # Append the bottom row of asterisks to 'result'
    result.append("*" * (col + 2))
    
    return result

# Code Sig Practice
