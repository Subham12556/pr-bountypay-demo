from auth import check_login


def test_valid_login():
    assert check_login("alice", "s3cret") is True


def test_wrong_password_rejected():
    assert check_login("alice", "s3cXXX") is False


def test_prefix_is_not_enough():
    assert check_login("alice", "s3c") is False


def test_unknown_user_rejected():
    assert check_login("mallory", "s3cret") is False


def test_empty_password_rejected():
    assert check_login("alice", "") is False
