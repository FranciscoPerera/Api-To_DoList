from db import get_connection

# LISTAR TODOS
def get_all_todos():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM todos ORDER BY id DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


# BUSCAR POR ID
def get_todo_by_id(todo_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    return row


# CRIAR
def create_todo(name, description):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO todos (name, description) VALUES (%s, %s)",
        (name, description)
    )

    conn.commit()
    cur.close()
    conn.close()


# ATUALIZAR
def update_todo(todo_id, name, description, completed):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE todos
        SET name=%s, description=%s, completed=%s
        WHERE id=%s
        """,
        (name, description, completed, todo_id)
    )

    conn.commit()
    cur.close()
    conn.close()


# DELETAR
def delete_todo(todo_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM todos WHERE id = %s", (todo_id,))

    conn.commit()
    cur.close()
    conn.close()