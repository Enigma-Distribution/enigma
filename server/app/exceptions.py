class EnigmaException(Exception):
    def __str__(self):
        return "Enigma Basic Exception"

class TaskNotFoundException(EnigmaException):
    def __str__(self):
        return "No such task found under with the user."

class PasswordMismatchException(EnigmaException):
    def __str__(self):
        return "Given password not matching with actual password."

class EmailAlreadyExistsException(EnigmaException):
    def __str__(self):
        return "This email is already registered."

class UsernameAlreadyExistsException(EnigmaException):
    def __str__(self):
        return "This username is already registered."

class SecretInvalidException(EnigmaException):
    def __str__(self):
        return "Password submitted was invalid. It must contain [0-9], [a-z], [A-Z], atleast one special character, " \
               "length between 8 to 32. "