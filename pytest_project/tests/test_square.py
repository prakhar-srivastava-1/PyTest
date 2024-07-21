import pytest
import source.shapes as shapes


# practise pytest-fixture
# going back to function-based tests
@pytest.fixture
def my_square():
    """demonstrates a fixture by arranging a square object

    Returns:
        square object: custom square object
    """
    return shapes.Square(10)


@pytest.fixture
def other_square():
    """demonstrates a fixture by arranging a different square object

    Returns:
        square object: custom square object
    """
    return shapes.Square(15)


def test_area(my_square):
    """checks the calculated area against expected area

    Args:
        my_square (PyTest Fixture): arranged square object
    """
    assert my_square.area() == 10 * 10


def test_perimeter(my_square):
    """checks the calculated perimter against expected area

    Args:
        my_square (PyTest Fixture): arranged square object
    """
    assert my_square.perimeter() == 4 * 10


# skip this test by using markers
@pytest.mark.skip(reason="partially implemented")
def test_area_equality(my_square, other_square):
    """checks if areas of square one and two are same

    Args:
        my_square (PyTest Fixture): arranged square object
        other_square (PyTest Fixture): arranged square object
    """
    assert my_square.area() == other_square.area()
