import source.service as service
import unittest.mock as mock


# mock the implementation of get_user_from_db
# pass the path to function in patch as argument
# the source function passed as argument is replaced
# by the mock function
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    """create a mock function called mock_get_user_from_db
    and patch it with the source function get_user_from_db
    which would imply, any call made to get_user_from_db
    will get redirected to mock_get_user_from_db

    Args:
        mock_get_user_from_db (mock function): mock function
    """
    # set the default return value for mock function
    mock_get_user_from_db.return_value = "Mocked Alice"
    # service.get_user_from_db(1) returns "Mocked Alice"
    # since this function has been patched
    user_name = service.get_user_from_db(1)
    # in the background, the call to get_user_from_db
    # is overriden by mock_get_user_from_db which simply
    # returns the hard-coded return_value
    assert user_name == "Mocked Alice"
