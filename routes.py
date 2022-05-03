import email
import sqlite3 as sql
import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('formulario.html')


@app.route('/escrever', methods=['POST', 'GET'])
def grava():
    email = request.form['email']
    nome = request.form['nome']
    endereco = request.form['endereco']

    if email and nome and endereco:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO usuarios (email, nome, endereco) VALUES (?,?,?)", (email, nome, endereco))

            con.commit()
            msg = "Informações inseridas com sucesso"
            return render_template("formulario.html", msg=msg)
            con.close()
    else:
        return("Algo saiu errado")


@app.route('/listar')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from usuarios")

    rows = cur.fetchall()
    return render_template("listar.html", rows=rows)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
