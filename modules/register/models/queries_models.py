class queries_users():
    def getUsers():
        queries = 'SELECT * FROM appl.appl_mst_user'
        return queries
    
    def insertUser():
        queries = 'INSERT INTO appl.appl_mst_user (user_fullname, user_username, user_password, user_role, created_by, created_date) VALUES (%s, %s, %s, %s, %s, %s)'
        return queries