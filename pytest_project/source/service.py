# a service that fetches user from a dummy database
database = {1: "Alice", 2: "Bob", 3: "Charlie"}


def get_user_from_db(user_id):
    """returns the user against user_id from database

    Args:
        user_id (int): primary key of User database

    Returns:
        str: User name
    """
    return database.get(user_id)
