from flask import Blueprint, jsonify

from business.service_task import ServiceTask

api_task_bp = Blueprint("api_task", __name__)


@api_task_bp.route("/api/task/<process_definition_id>")
def get_list(process_definition_id: str):
    results = ServiceTask.get_task_list(process_definition_id)
    return jsonify(results)


@api_task_bp.route("/api/variable/<process_definition_id>")
def get_variable_list(process_definition_id: str):
    results = ServiceTask.get_variables_list(process_definition_id)
    return jsonify(results)
