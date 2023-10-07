
def area_of_rectangle(width: int | float, height: int | float) -> int | float:
    """Computes the area of the rectangle
    
    This function computes the area of the rectangle with given width and height.
    
    Args:
        width: Integer or float
        height: Integer or float
    
    Returns:
        The area of the rectangle as a float or integer
    """
    return width*height

def perimeter_of_rectangle(width: int | float, height: int | float) -> int | float:
    """Computes the perimeter of the rectangle
    
    This function computes the perimeter of the rectangle with given width and height.
    
    Args:
        width: Integer or float
        height: Integer or float
    
    Returns:
        The perimeter of the rectangle as a float or integer
    """
    return 2*width + 2*height