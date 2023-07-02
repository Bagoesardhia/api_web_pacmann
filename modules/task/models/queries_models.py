class queries_task():
    def getAll():
        queries = 'SELECT * FROM appl.appl_main_task order by project_id'
        return queries
    
    def getTaskname():
        queries = 'SELECT project_id FROM appl.appl_main_task order by project_id'
        return queries
    
    def getTaskID(p_id):
        queries = f"SELECT * FROM appl.appl_main_task where project_id = '{p_id}'"
        return queries

    def insertTask():
        queries = 'INSERT INTO appl.appl_main_task (project_id, project_name, project_desc, project_start, project_end, created_by, created_date, project_owner, project_asign, project_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        return queries
    
    def updateTask():
        queries = 'UPDATE appl.appl_main_task SET project_desc = %s, project_start = %s, project_end = %s, updated_by = %s, updated_date = %s, project_asign = %s, project_status = %s where project_id = %s '
        return queries
