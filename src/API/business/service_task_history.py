from scripts.script_loader import ScriptLoader
from util.database import Database


class ServiceTaskHistory:
    @staticmethod
    def get_task_history_list(process_instance_id: str) -> list[dict]:
        d = Database().get_database()
        query = ScriptLoader().task_history()
        params = {"process_instance_id": process_instance_id}
        result = d.execute_sql_with_dict_result(query, params)
        return result

    @staticmethod
    def get_process_instance_variables(process_instance_id: str) -> list[dict]:
        d = Database().get_database()
        query = ScriptLoader().task_history_variables()
        params = {"process_instance_id": process_instance_id}
        results_as_list_of_dictionary = d.execute_sql_with_dict_result(query, params)
        results_as_dictionary = {}
        for item in results_as_list_of_dictionary:
            results_as_dictionary[item["Name"]] = item["Value"]
        return [results_as_dictionary]
