def load_file(filename: str) -> str:
    with open(f'./scripts/postgres/{filename}', 'r') as file_handle:
        script = file_handle.read()
        return script


class ScriptLoader:

    @staticmethod
    def process_definition():
        return load_file('process_definition.sql')

    @staticmethod
    def variable_list():
        return load_file('variable_list.sql')

    @staticmethod
    def task():
        return load_file('task.sql')

    @staticmethod
    def task_history():
        return load_file('task_history.sql')

    @staticmethod
    def task_history_variables():
        return load_file('task_history_variables.sql')
