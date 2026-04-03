import sys, os, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from db import get_connection, create_users_table, insert_user

def test_insert_user():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = f.name
    conn = get_connection(db_path)
    create_users_table(conn)
    # This should fail due to wrong column name in insert_user
    insert_user(conn, "alice", "hash123")
    conn.close()
