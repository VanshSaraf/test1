# 09-multi-error

## What this repo tests
AtlasOps ability to handle **multiple layered errors** across two files.

## What is intentionally broken

### Error 1 — `src/auth.py` line 18: SyntaxError
```python
def generate_token()   # Missing colon
```

### Error 2 — `src/auth.py` line 3: Unused import (flake8 F401)
```python
import datetime   # Never used
```

### Error 3 — `src/db.py` line 24: Wrong column name in SQL
```python
"INSERT INTO users (username, passwd_hash) VALUES (?, ?)"
# Should be: password_hash
```

## Expected AtlasOps behavior
- **Detect:** SyntaxError blocks all tests; flake8 also reports F401
- **Fix (ordered):**
  1. Add `:` to `generate_token()` definition
  2. Remove unused `datetime` import
  3. Fix SQL column name `passwd_hash` → `password_hash`
- **Rerun:** All 3 tests pass
- **Difficulty:** Hard
