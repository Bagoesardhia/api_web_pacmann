class queries_task():
    def getAll():
        queries = 'SELECT * FROM appl.appl_main_task'
        return queries

    def insertTask():
        queries = 'INSERT INTO appl.appl_main_task (project_name, project_desc, project_start, project_end) VALUES (%s,%s,%s,%s)'
        return queries
