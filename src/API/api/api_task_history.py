from flask import Blueprint, jsonify

from business.service_task_history import ServiceTaskHistory

api_task_history_bp = Blueprint("api_task_history", __name__)


@api_task_history_bp.route("/api/task-history/<process_instance_id>")
def get_list(process_instance_id: str):
    results = ServiceTaskHistory.get_task_history_list(process_instance_id)
    return jsonify(results)


@api_task_history_bp.route("/api/task-history/<process_instance_id>/variables")
def get_variables(process_instance_id: str):
    results = ServiceTaskHistory.get_process_instance_variables(process_instance_id)
    return jsonify(results)
