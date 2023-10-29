import json

from api.init import create_app

app = create_app()


def get_config() -> dict:
    with open("config.json", "r") as file_handle:
        config_dict = json.load(file_handle)
    return config_dict


if __name__ == '__main__':
    config = get_config()
    app.run(**config)
