from flask import Blueprint, jsonify

spa_bp = Blueprint("spa", __name__, static_folder="static", static_url_path="/static")

@spa_bp.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})

@spa_bp.route("/", defaults={"path": ""})
@spa_bp.route("/<path:path>")
def catch_all(path: str):
    if is_static_file(path):
        return spa_bp.send_static_file(path)

    return spa_bp.send_static_file("index.html")


def is_static_file(path: str) -> bool:
    static_files_extension_list = ["png", "ico", "js", "css"]
    for static_file_extension in static_files_extension_list:
        if path.endswith(static_file_extension):
            return True

    return False
