"""
Chapter 1: Vector addition and scalar multiplication
    Tests
"""
# Import 
from vectors import add

# 1. Vector addition test
def test_add_basics():
    # Vectors definition
    v = [1, 2]
    u = [3, -1]

    # Expected output
    expected = [4, 1]
    
    # Testing
    assert add(v, u) == expected