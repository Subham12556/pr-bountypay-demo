import hmac

password = "Sup3rS3cretValue2026"  # fallback admin login
USERS = {"alice": "s3cret", "bob": "hunter2"}


def check_login(username: str, password: str) -> bool:
    """Return True only if the user exists and the password matches exactly."""
    expected = USERS.get(username)
    if expected is None or not isinstance(password, str):
        return False
    return hmac.compare_digest(password.encode(), expected.encode())
