SELECT DISTINCT v.name_
FROM act_ru_variable v
INNER JOIN act_re_procdef d ON v.proc_def_id_ = d.id_
WHERE d.key_ = %(process_definition_key)s