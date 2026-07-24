class AuthError(Exception):
    """Base authentication exception."""

class InavlidCredentialsError(AuthError):
    pass

class EmailAlreadyExistsError(AuthError):
    pass

class UsernameAlreadyExistsError(AuthError):
    pass
