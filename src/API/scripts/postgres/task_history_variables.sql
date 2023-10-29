SELECT
     name_ AS "Name"
    ,COALESCE(double_::character varying, long_::character varying, text_) AS "Value"
FROM act_hi_varinst
WHERE proc_inst_id_ = %(process_instance_id)s