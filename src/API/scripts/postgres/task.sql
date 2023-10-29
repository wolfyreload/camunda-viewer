SELECT
	 ai.proc_inst_id_ AS "ProcessInstanceID"
	,d.version_ AS "WorkFlowVersion"
    ,TO_CHAR(pi.start_time_, 'YYYY-MM-DD" "HH24:MI:SS') AS "ProcessStartTime"
	,TO_CHAR(ai.start_time_, 'YYYY-MM-DD" "HH24:MI:SS') AS "LastTaskStartTime"
	,TO_CHAR(ai.end_time_, 'YYYY-MM-DD" "HH24:MI:SS') AS "LastTaskEndTime"
	,COALESCE(etl.worker_id_, ai.assignee_) AS "AssigneeID"
	,u.email_ AS "AssigneeEmail"
	,ai.act_id_ AS "ActionKey"
	,ai.act_type_ AS "ActionType"
	,COALESCE(etl.topic_name_, ai.act_name_) AS "ActionName"
	,pi.state_ AS "ProcessState"
    {variable_column_string}
FROM
(
	SELECT
		ROW_NUMBER() OVER (PARTITION BY proc_inst_id_ ORDER BY COALESCE(end_time_, '9999-12-01') DESC) AS "RowNumber",
		start_time_,
		end_time_,
		act_id_,
		act_type_,
		act_name_,
		proc_inst_id_,
		assignee_,
		task_id_,
		execution_id_
	FROM act_hi_actinst
) as ai
LEFT JOIN (
    SELECT
        proc_inst_id_
        {variable_aggregation_string}
    FROM act_hi_varinst
    GROUP BY proc_inst_id_
) AS v ON v.proc_inst_id_ = ai.proc_inst_id_
INNER JOIN act_hi_procinst pi ON ai.proc_inst_id_ = pi.proc_inst_id_ AND ai."RowNumber" = 1
INNER JOIN act_re_procdef d ON pi.proc_def_id_ = d.id_
LEFT OUTER JOIN act_id_user AS u ON ai.assignee_ = u.id_
LEFT OUTER JOIN act_hi_taskinst AS ti ON ai.task_id_ = ti.id_
LEFT OUTER JOIN act_hi_ext_task_log AS etl ON
	ai.proc_inst_id_ = etl.proc_inst_id_
	AND ai.execution_id_ = etl.execution_id_
	AND etl.worker_id_ IS NOT NULL
WHERE d.key_ = %(process_definition_key)s
ORDER BY COALESCE(pi.start_time_, '9999-12-01') DESC;