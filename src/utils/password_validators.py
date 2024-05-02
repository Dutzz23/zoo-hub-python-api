def validate_password(password: str) -> None:
    try:
        if len(password) < 8:
            raise Exception('Password must be at least 8 characters long')
        if len(password) > 32:
            raise Exception('Password must be less than 32 characters long')
        if not any(c.isupper() for c in password):
            raise Exception("Password must have at least one uppercase letter")
        if not any(c.islower() for c in password):
            raise Exception("Password must have at least one lowercase letter")
        if not any(c.isdigit() for c in password):
            raise Exception("Password must have at least one digit")
    except Exception as e:
        raise Exception(f"Password validation error: {e}")


def verify_password(password: str, hashed_password: str) -> None:
    if password != hashed_password:
        raise Exception("Invalid password")