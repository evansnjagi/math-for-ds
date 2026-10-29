"""
Chapter 1: Vectors
    Vector addition and scalar multiplication
"""
# Vector addition 
def add(u: list[float], v: list[float]) -> list[float]:
    """
    Return the element-wise sum of two vectors of the same length, i.e. they live in the same space.

    Parameters:
    -----------
    u: list[float]
        A list of items, first vector.
    v: list[float]
        A list of items, second vector.

    Returns
    -------
    list[float]
        Addition of the two vectors, u + v.

    Raises
    ------
    ValueError
        Raised when  the two vectors, u and v, have different lengths.
    """
    # Validate length
    if len(v) != len(u):
        raise ValueError(f"Vectors must have the same length, got {len(v)} and {len(u)}")
    
    # Create an empty list
    result = []

    # Loop
    for i in range(len(v)):
        result.append(u[i] + v[i])

    # Return 
    return result
