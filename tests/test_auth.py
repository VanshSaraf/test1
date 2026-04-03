import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# This import itself will fail due to SyntaxError in auth.py
from auth import hash_password, verify_password

def test_password_roundtrip():
    stored = hash_password("mysecret")
    assert verify_password("mysecret", stored) is True

def test_wrong_password_rejected():
    stored = hash_password("mysecret")
    assert verify_password("wrongpassword", stored) is False
