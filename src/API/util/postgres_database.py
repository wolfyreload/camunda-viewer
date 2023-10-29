from collections import OrderedDict
from itertools import chain

import psycopg2


class PostgresDatabase:
    def __init__(self, connection_details):
        self.connection_details = connection_details

    def execute_sql_with_list_result(self, query: str, parameters=None) -> list:
        """
        Execute query and return results as a list

        :param query: the query string
        :param parameters: query parameters
        :return: list
        """
        with psycopg2.connect(**self.connection_details) as connection:
            cursor = self.get_query_cursor(connection, query, parameters)
            result_set = cursor.fetchall()
            list_of_results = list(chain(*result_set))
            return list_of_results

    def execute_sql_with_dict_result(self, query: str, parameters=None) -> list[dict]:
        """
        Execute query and return list of dictionary results

        :param query: the query string
        :param parameters: query parameters
        :return: list[dict]
        """
        with psycopg2.connect(**self.connection_details) as connection:
            cursor = self.get_query_cursor(connection, query, parameters)

            # Fetch all the rows and store them in a list of dictionaries
            result_set = []
            columns = [column[0] for column in cursor.description]

            for row in cursor.fetchall():
                zipped = zip(columns, row)
                dictionary = OrderedDict(zipped)
                result_set.append(dictionary)

            return result_set

    @staticmethod
    def get_query_cursor(connection, query: str, parameters=None):
        cursor = connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        return cursor
