"""
Security-related helpers for Project Aurora.
Includes basic validation and access checks.
"""

def validate_input(value):
    if not value:
        return False
    if isinstance(value, str) and len(value.strip()) == 0:
        return False
    return True

def has_access(user_role, required_role):
    roles = ["guest", "user", "admin"]
    return roles.index(user_role) >= roles.index(required_role)
