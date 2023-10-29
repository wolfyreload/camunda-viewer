from flask import Blueprint, jsonify

from util.service_environment import ServiceEnvironment

api_environment_bp = Blueprint("api_environment", __name__)


@api_environment_bp.route("/api/environment")
def get_environments():
    environment_list = ServiceEnvironment.get_environment_list()
    return jsonify(environment_list)


@api_environment_bp.route("/api/environment/<environment_id>", methods=["POST"])
def set_environment(environment_id):
    ServiceEnvironment.set_current_environment(environment_id)
    return jsonify("")
