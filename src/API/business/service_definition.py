from scripts.script_loader import ScriptLoader
from util.database import Database


class ServiceDefinition:
    @staticmethod
    def get_camunda_definitions():
        d = Database().get_database()
        query = ScriptLoader().process_definition()
        results = d.execute_sql_with_dict_result(query)
        return results
