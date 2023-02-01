class ApiError(Exception):
    code = 422
    description = "Default message"

class UserAlreadyExists(ApiError):
    code = 412
    description = "User with username or email already exists"

class InvalidParams(ApiError):
    code = 400
    description = "Bad request"
