from connection.connection import conn
from ..models.query_models import queries_login, queries_last_open
from datetime import datetime

from flask import jsonify

class logincontroller():
    def main_login(p_user, p_pass):
        v_user = logincontroller.check_users(p_user, p_pass)
        if v_user != None :
            print('user: ',v_user)  
            v_data = {'Status':'Login Berhasil',
                      'Data': v_user
                    }
            return 0
        else:
            v_data = {'Status':'Login Failed',
                      'Data': v_user
                      }
            return 1


    def check_users(p_user, p_pass):
        try:
            cursor = conn.cursor()
            queries = queries_login()
            cursor.execute(queries,(p_user,p_pass))
            data = cursor.fetchone()
            if data != None:
                return data
            else:
                return data
        except Exception as e:
            print('err', e)
            return 1
        
        ## Logic Last Open
    def update_last_open():
        try:
            new_timestamp = '2023-06-22 21:15:19' ##datetime.now()
            cursor = conn.cursor()
            queries = queries_last_open()
            cursor.execute(queries, (new_timestamp))
            conn.commit()
            return 0
        except Exception as e:
            data = 'err', e
            return data