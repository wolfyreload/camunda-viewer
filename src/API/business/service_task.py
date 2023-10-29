from scripts.script_loader import ScriptLoader
from util.database import Database


class ServiceTask:
    @staticmethod
    def get_variables_list(process_definition_key: str) -> list:
        d = Database().get_database()
        query = ScriptLoader().variable_list()
        params = {"process_definition_key": process_definition_key}
        result = d.execute_sql_with_list_result(query, params)
        return result

    @staticmethod
    def get_variable_column_string(variable_list) -> str:
        if len(variable_list) == 0:
            return ""
        column_list = []
        for variable_name in variable_list:
            column_list.append(f',v."Variable_{variable_name}"\n')
        result = "".join(column_list)
        return result

    @staticmethod
    def get_variable_aggregation_string(variable_list) -> str:
        if len(variable_list) == 0:
            return ""
        column_list = []
        for variable_name in variable_list:
            column_list.append(
                f",MAX(CASE WHEN name_ = '{variable_name}' THEN COALESCE(double_::character varying, long_::character varying, text_) END) AS \"Variable_{variable_name}\"\n"
            )
        result = "".join(column_list)
        return result

    @staticmethod
    def get_task_list(process_definition_key: str) -> list[dict]:
        variable_list = ServiceTask.get_variables_list(process_definition_key)
        variable_column_string = ServiceTask.get_variable_column_string(variable_list)
        variable_aggregation_string = ServiceTask.get_variable_aggregation_string(
            variable_list
        )

        d = Database().get_database()
        query = ScriptLoader().task()
        query = query.replace("{variable_column_string}", variable_column_string)
        query = query.replace(
            "{variable_aggregation_string}", variable_aggregation_string
        )
        params = {"process_definition_key": process_definition_key}
        result = d.execute_sql_with_dict_result(query, params)
        return result
