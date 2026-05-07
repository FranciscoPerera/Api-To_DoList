from flask import Blueprint, request, jsonify
from models.tarefa_model import *

task_bp = Blueprint("task_bp", __name__)


# STATUS API
@task_bp.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "API de Lista de Tarefas rodando!!"})

# LISTAR
@task_bp.route("/api/tarefas", methods=["GET"])
def list_tasks():
    tasks = get_all_tasks()

    return jsonify([
        {
            "id": t[0],
            "nome": t[1],
            "descricao": t[2],
            "status": t[3],
            "criado_em": t[4]
        }
        for t in tasks
    ])

# BUSCAR
@task_bp.route("/api/tarefas/<int:task_id>", methods=["GET"])
def get_task(task_id):
    t = get_task_by_id(task_id)

    if not t:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    return jsonify({
        "id": t[0],
        "nome": t[1],
        "descricao": t[2],
        "status": t[3],
        "criado_em": t[4]
    })

# CRIAR
@task_bp.route("/api/tarefas", methods=["POST"])
def create():
    data = request.get_json()

    create_task(
        data["nome"],
        data.get("descricao")
    )

    return jsonify({"message": "Tarefa criada com sucesso"}), 201

# ATUALIZAR
@task_bp.route("/api/tarefas/<int:task_id>", methods=["PUT"])
def update(task_id):
    data = request.get_json()

    update_task(
        task_id,
        data["nome"],
        data.get("descricao"),
        data.get("status", False)
    )

    return jsonify({"message": "Tarefa atualizada com sucesso"})

# DELETAR
@task_bp.route("/api/tarefas/<int:task_id>", methods=["DELETE"])
def delete(task_id):
    delete_task(task_id)

    return jsonify({"message": "Tarefa deletada com sucesso"})