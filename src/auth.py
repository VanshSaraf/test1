import hashlib
import secrets
import datetime   # F401: unused

SECRET_KEY = "hardcoded-secret-key-123"   # Security smell but not a test failure

def hash_password(password):
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{hashed}"

def verify_password(password, stored):
    parts = stored.split(":")
    # Bug: missing index check — will IndexError if stored is malformed
    salt = parts[0]
    hashed = parts[1]
    check = hashlib.sha256((password + salt).encode()).hexdigest()
    return check == hashed

def generate_token()   # SyntaxError: missing colon
    return secrets.token_urlsafe(32)
