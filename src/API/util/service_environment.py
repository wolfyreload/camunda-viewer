import os


class ServiceEnvironment:
    selected_environment_name = ""

    @classmethod
    def get_environment_list(cls) -> list[dict]:
        file_name_list = os.listdir("./environments")
        results = []
        for file_name in file_name_list:
            if file_name == ".gitkeep":
                continue
            if "example" in file_name:
                continue
            file_name = file_name.replace(".json", "")
            results.append({"EnvironmentName": file_name})
        return results

    @classmethod
    def set_current_environment(cls, environment_name):
        cls.selected_environment_name = environment_name
