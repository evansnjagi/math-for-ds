"""
Chapter 1: Vector addition and scalar multiplication
    Tests
"""
# Import 
import pytest

from vectors import add, scale

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

# 3. Test vector-scalar multiplication
def test_scale_basic():
   assert scale(2, [1, -3]) == [2, -6]

# 4. Test for floating point numbers
def test_scale_float():
    assert scale(0.1, [3]) == pytest.approx([0.3])

# 5. Test that scale does not modify the input
def test_scale_does_not_modify_input():
    # Arrange
    original = [1, 2, 3]
    v = [1, 2, 3]

    # Act
    result = scale(2, v)

    # Assert
    assert v == original
    assert result == [2, 4, 6]