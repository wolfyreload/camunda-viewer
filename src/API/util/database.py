import json

from util.service_environment import ServiceEnvironment
from util.postgres_database import PostgresDatabase
from util.sqlserver_database import SQLServerDatabase


def get_connection_string_from_config():
    environment_name = ServiceEnvironment.selected_environment_name
    config_location = f"./environments/{environment_name}.json"
    with open(config_location, "r") as file:
        data = json.load(file)
    return data


class Database:
    @staticmethod
    def get_database():
        connection_details = get_connection_string_from_config()
        if connection_details["driver"] == "postgresql":
            del connection_details["driver"]
            return PostgresDatabase(connection_details)
        if connection_details["driver"] == "ODBC Driver 18 for SQL Server":
            return SQLServerDatabase(connection_details)
