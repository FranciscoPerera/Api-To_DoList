from flask import Blueprint, request, jsonify
from models.todo_model import *

todo_bp = Blueprint("todo_bp", __name__)


# HELLO
@todo_bp.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "API de Tarefas rodando 🚀"})


# LISTAR
@todo_bp.route("/api/todos", methods=["GET"])
def list_todos():
    todos = get_all_todos()

    return jsonify([
        {
            "id": t[0],
            "name": t[1],
            "description": t[2],
            "completed": t[3],
            "created_at": t[4]
        }
        for t in todos
    ])


# BUSCAR POR ID
@todo_bp.route("/api/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    t = get_todo_by_id(todo_id)

    if not t:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    return jsonify({
        "id": t[0],
        "name": t[1],
        "description": t[2],
        "completed": t[3],
        "created_at": t[4]
    })


# CRIAR
@todo_bp.route("/api/todos", methods=["POST"])
def create():
    data = request.get_json()

    create_todo(data["name"], data.get("description"))

    return jsonify({"message": "Tarefa criada com sucesso"}), 201


# ATUALIZAR
@todo_bp.route("/api/todos/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    data = request.get_json()

    update_todo(
        todo_id,
        data["name"],
        data.get("description"),
        data.get("completed", False)
    )

    return jsonify({"message": "Tarefa atualizada"})


# DELETAR
@todo_bp.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete(todo_id):
    delete_todo(todo_id)

    return jsonify({"message": "Tarefa deletada"})