from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name)

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jardel123",
    database="projeto"
)

cursor = conn.cursor()

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    data = request.json
    nome = data['nome']
    idade = data['idade']
    nota_primeiro_semestre = data['nota_primeiro_semestre']
    nota_segundo_semestre = data['nota_segundo_semestre']
    nome_professor = data['nome_professor']
    numero_sala = data['numero_sala']
    
    sql = "INSERT INTO alunos (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala)
    cursor.execute(sql, val)
    conn.commit()
    return jsonify({"message": "Aluno inserido com sucesso!"})

@app.route('/alunos', methods=['GET'])
def obter_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    alunos_list = []
    for aluno in alunos:
        aluno_dict = {
            "ID": aluno[0],
            "nome": aluno[1],
            "idade": aluno[2],
            "nota_primeiro_semestre": float(aluno[3]),
            "nota_segundo_semestre": float(aluno[4]),
            "nome_professor": aluno[5],
            "numero_sala": aluno[6]
        }
        alunos_list.append(aluno_dict)
    return jsonify(alunos_list)

# Outras rotas para atualização e exclusão de alunos podem ser adicionadas aqui

if __name__ == '__main__':
    app.run(debug=True)
