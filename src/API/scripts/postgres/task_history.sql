SELECT
	 TO_CHAR(ai.start_time_, 'YYYY-MM-DD" "HH24:MI:SS') AS "StartTime"
	,TO_CHAR(ai.end_time_, 'YYYY-MM-DD" "HH24:MI:SS') AS "EndTime"
	,COALESCE(etl.worker_id_, ai.assignee_) AS "AssigneeID"
	,u.email_ AS "AssigneeEmail"
	,ai.act_id_ AS "ActionKey"
	,ai.act_type_ AS "ActionType"
	,COALESCE(etl.topic_name_, ai.act_name_) AS "ActionName"
FROM act_hi_actinst ai
LEFT OUTER JOIN act_id_user AS u ON ai.assignee_ = u.id_
LEFT OUTER JOIN act_hi_taskinst AS ti ON ai.task_id_ = ti.id_
LEFT OUTER JOIN act_hi_ext_task_log AS etl ON
	ai.proc_inst_id_ = etl.proc_inst_id_
	AND ai.execution_id_ = etl.execution_id_
	AND etl.worker_id_ IS NOT NULL
WHERE ai.proc_inst_id_ = %(process_instance_id)s
ORDER BY COALESCE(ai.end_time_, '9999-12-01') DESC