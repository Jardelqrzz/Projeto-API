import mysql.connector

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jardel123",
    database="projeto"
)

cursor = conn.cursor()

def criar_aluno(nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala):
    sql = "INSERT INTO alunos (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala)
    cursor.execute(sql, val)
    conn.commit()
    print("Aluno inserido com sucesso!")

def ler_aluno(id):
    sql = "SELECT * FROM alunos WHERE ID = %s"
    val = (id,)
    cursor.execute(sql, val)
    aluno = cursor.fetchone()
    if aluno:
        print("ID:", aluno[0])
        print("Nome:", aluno[1])
        print("Idade:", aluno[2])
        print("Nota do primeiro semestre:", aluno[3])
        print("Nota do segundo semestre:", aluno[4])
        print("Nome do professor:", aluno[5])
        print("Número da sala:", aluno[6])
    else:
        print("Aluno não encontrado!")

def atualizar_aluno(id, nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala):
    sql = "UPDATE alunos SET nome = %s, idade = %s, nota_primeiro_semestre = %s, nota_segundo_semestre = %s, nome_professor = %s, numero_sala = %s WHERE ID = %s"
    val = (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala, id)
    cursor.execute(sql, val)
    conn.commit()
    print("Aluno atualizado com sucesso!")

def deletar_aluno(id):
    sql = "DELETE FROM alunos WHERE ID = %s"
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()
    print("Aluno excluído com sucesso!")


cursor.close()
conn.close()
