from db import get_connection

# LISTAR
def get_all_tasks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM lista_tarefas ORDER BY id DESC")
    tasks = cur.fetchall()

    cur.close()
    conn.close()

    return tasks

# BUSCAR POR ID
def get_task_by_id(task_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM lista_tarefas WHERE id = %s", (task_id,))
    task = cur.fetchone()

    cur.close()
    conn.close()

    return task

# CRIAR
def create_task(nome, descricao):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO lista_tarefas (nome, descricao) VALUES (%s, %s)",
        (nome, descricao)
    )

    conn.commit()
    cur.close()
    conn.close()

# ATUALIZAR
def update_task(task_id, nome, descricao, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE lista_tarefas
        SET nome=%s,
            descricao=%s,
            status=%s
        WHERE id=%s
        """,
        (nome, descricao, status, task_id)
    )

    conn.commit()
    cur.close()
    conn.close()

# DELETAR
def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM lista_tarefas WHERE id = %s", (task_id,))

    conn.commit()
    cur.close()
    conn.close()