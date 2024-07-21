import pytest
import source.shapes as shapes


# practise pytest-fixture
# going back to function-based tests
@pytest.fixture
def my_rectangle():
    """demonstrates a fixture by arranging a rectangle object

    Returns:
        Rectangle object: custom rectangle object
    """
    return shapes.Rectangle(10, 20)


@pytest.fixture
def other_rectangle():
    """demonstrates a fixture by arranging a different rectangle object

    Returns:
        Rectangle object: custom rectangle object
    """
    return shapes.Rectangle(15, 20)


def test_area(my_rectangle):
    """checks the calculated area against expected area

    Args:
        my_rectangle (PyTest Fixture): arranged rectangle object
    """
    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    """checks the calculated perimter against expected area

    Args:
        my_rectangle (PyTest Fixture): arranged rectangle object
    """
    assert my_rectangle.perimeter() == 2 * (10 + 20)


def test_area_equality(my_rectangle, other_rectangle):
    """checks if areas of rectangle one and two are same

    Args:
        my_rectangle (PyTest Fixture): arranged rectangle object
        other_rectangle (PyTest Fixture): arranged rectangle object
    """
    assert my_rectangle.area() == other_rectangle.area()
