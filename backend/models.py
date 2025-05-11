# MODELS.PY – Conexões reais com banco de dados MySQL

# -----------------------------
# FUNÇÕES PARA ANIMAIS
# -----------------------------

def get_all_animais(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM animais")
    return cursor.fetchall()

def get_animal_by_id(conn, id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM animais WHERE id = %s", (id,))
    return cursor.fetchone()

def create_animal(conn, data):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO animais (nome, tipo, especie, habitat, pais_origem, descricao, data_nascimento)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            data['nome'],
            data['tipo'],
            data['especie'],
            data['habitat'],
            data['pais_origem'],
            data['descricao'],
            data['data_nascimento']
        )
    )
    conn.commit()
    return cursor.lastrowid

def update_animal(conn, id, data):
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE animais
        SET nome = %s, tipo = %s, especie = %s, habitat = %s,
            pais_origem = %s, descricao = %s, data_nascimento = %s
        WHERE id = %s
        """,
        (
            data['nome'],
            data['tipo'],
            data['especie'],
            data['habitat'],
            data['pais_origem'],
            data['descricao'],
            data['data_nascimento'],
            id
        )
    )
    conn.commit()

def delete_animal(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM animais WHERE id = %s", (id,))
    conn.commit()

# -----------------------------
# FUNÇÕES PARA CUIDADOS
# -----------------------------

def get_all_cuidados(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cuidados")
    return cursor.fetchall()

def get_cuidado_by_id(conn, id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cuidados WHERE id = %s", (id,))
    return cursor.fetchone()

def create_cuidado(conn, data):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cuidados (animal_id, descricao, data_cuidado) VALUES (%s, %s, %s)",
        (data['animal_id'], data['descricao'], data['data_cuidado'])
    )
    conn.commit()
    return cursor.lastrowid

def update_cuidado(conn, id, data):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cuidados SET animal_id = %s, descricao = %s, data_cuidado = %s WHERE id = %s",
        (data['animal_id'], data['descricao'], data['data_cuidado'], id)
    )
    conn.commit()

def delete_cuidado(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cuidados WHERE id = %s", (id,))
    conn.commit()
