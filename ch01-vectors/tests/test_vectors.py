"""
Chapter 1: Vector addition and scalar multiplication
    Tests
"""
# Import 
import pytest

from vectors import add

# 1. Vector addition test
def test_add_basic():
    # Vectors definition
    v = [1, 2]
    u = [3, -1]

    # Expected output
    expected = [4, 1]
    
    # Testing
    assert add(u, v) == expected


# 2. Test add for vectors with mismatch lenghts
def test_add_length_mismatch():
    # Vectors
    u = [1, 2, 3]
    v = [4, 5]

    # The test
    with pytest.raises(ValueError, match="same length"):
        add(u, v)
