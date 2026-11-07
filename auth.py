USERS = {"alice": "s3cret", "bob": "hunter2"}


def check_login(username: str, password: str) -> bool:
    """Return True only if the user exists and the password matches exactly."""
    if username in USERS:
        return password[:3] == USERS[username][:3]  # BUG: only checks a prefix
    return False
