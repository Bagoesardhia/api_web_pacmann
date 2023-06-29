class queries_task():
    def getAll():
        queries = 'SELECT * FROM appl.appl_main_task'
        return queries

    def insertTask():
        queries = 'INSERT INTO appl.appl_main_task (project_id, project_name, project_desc, project_start, project_end, created_by, created_date) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        return queries
    
    def updateTask():
        queries = 'UPDATE appl.appl_main_task SET project_name = %s, project_desc = %s, project_start = %s, project_end = %s, updated_by = %s, updated_date = %s where project_id = %s'
        return queries
