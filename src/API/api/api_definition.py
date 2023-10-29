from flask import Blueprint, jsonify

from business.service_definition import ServiceDefinition

api_definition_bp = Blueprint("api_definition", __name__)


@api_definition_bp.route("/api/definition")
def get_list():
    results = ServiceDefinition.get_camunda_definitions()
    return jsonify(results)
