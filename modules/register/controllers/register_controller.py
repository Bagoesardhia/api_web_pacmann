from connection.connection import conn
from ..models.queries_models import queries_users

class registerController():
    def main(p_type, p_name, p_username, p_password, p_role, p_created_by, p_created_date):
        if p_type == 'A':
            retval = registerController.getUsers()
        elif p_type == 'N':
            retval = registerController.newUsers(p_name, p_username, p_password, p_role, p_created_by, p_created_date)
        return retval
    
    def getUsers():
        try:
            cursor = conn.cursor()
            queries = queries_users.getUsers()
            cursor.execute(queries)
            data = cursor.fetchall()
            data_list = []
            for row in data:
                data_dict = {
                    'userid': row[0],
                    'username': row[2],
                    'userid': row[4],
                }
                data_list.append(data_dict)
            return data_list
        except Exception as e:
            retval = {'Err':str(e)
                    }
            return retval
        
    def newUsers(p_name, p_username, p_password, p_role, p_created_by, p_created_date):
        try:
            cursor = conn.cursor()
            queries = queries_users.insertUser()
            cursor.execute(queries, (p_name, p_username, p_password, p_role, p_created_by, p_created_date))
            conn.commit()
            v_data = {'Status':'User Berhasil Ditambahkan',
                      'Fullname': p_name,
                      'Username': p_username,
                      'Password': p_password,
                      'Role': p_role,
                    }
            return v_data
        except Exception as e:
            retval = {'Err':str(e)
                    }
            return retval