from connection.connection import conn
from ..models.queries_models import queries_task


class taskController():
    def main_task(p_type, p_id, p_project, p_desc, p_start, p_end, p_createby, p_createdate, p_updateby, p_updatedate, p_owner, p_asign, p_status):
        
        ## CREATE NEW TASK
        if p_type == 'N':
            v_data = taskController.insert_task(p_id, p_project, p_desc, p_start, p_end, p_createby, p_createdate, p_owner, p_asign, p_status)
        ## UPDATED TASK
        elif p_type == 'U':
            v_data = taskController.updateTask(p_desc, p_start, p_end, p_updateby, p_updatedate , p_asign, p_status, p_id)
        ## GET ALL TASKS
        elif p_type == 'A':
            v_data = taskController.get_task()
        ## GET TASK BY ID
        elif p_type == 'AD':
            v_data = taskController.getTaskID(p_id)
        ## GET TASK ONLY PROJECT NAME
        elif p_type == 'AN':
            v_data = taskController.get_task_v1()    
        return v_data

    def check_task():
        None
    
    def get_task():
        try:
            cursor = conn.cursor()
            queries = queries_task.getAll()
            cursor.execute(queries)
            data = cursor.fetchall()
            data_list = []
            for row in data:
                data_dict = {
                    'id': row[0],
                    'name': row[1],
                    'desc': row[2],
                    'start': row[3],
                    'end': row[4],
                    'auth':row[9],
                    'assign': row[10],
                    'status': row[11],
                }
                data_list.append(data_dict)
            return data_list
        except Exception as e:
            v_data = {'Err':str(e)
                    }
            return v_data
    
    def get_task_v1():
        try:
            cursor = conn.cursor()
            queries = queries_task.getTaskname()
            cursor.execute(queries)
            data = cursor.fetchall()
            data_list = []
            for row in data:
                data_dict = {
                    'id': row[0]
                }
                data_list.append(data_dict)
            return data_list
        except Exception as e:
            v_data = {'Err':str(e)
                    }
            return v_data
            

    def insert_task(p_id, p_project, p_desc, p_start, p_end, p_createby, p_createdate, p_owner, p_asign, p_status):
        try:
            cursor = conn.cursor()
            queries = queries_task.insertTask()
            cursor.execute(queries, (p_id, p_project, p_desc, p_start, p_end, p_createby, p_createdate, p_owner, p_asign, p_status))
            conn.commit()
            v_data = {'Status':'Task Berhasil Ditambahkan',
                      'Project Name': p_project,
                      'Project Desc': p_desc,
                      'Project Start': p_start,
                      'Project End': p_end,
                    }
            return v_data
        except Exception as e:
            v_data = {'Status':'Error Inserting Task',
                      'Project Name': p_project,
                      'Project Desc': p_desc,
                      'Project Start': p_start,
                      'Project End': p_end,
                      'Err Code': str(e)
                    }
            return v_data
    
    def updateTask(p_desc, p_start, p_end, p_updateby, p_updatedate , p_asign, p_status, p_id):
        try:
            cursor = conn.cursor()
            queries = queries_task.updateTask()
            cursor.execute(queries, (p_desc, p_start, p_end, p_updateby, p_updatedate, p_asign, p_status, p_id))
            conn.commit()
            v_data = {'Status':'Task Berhasil Di update',
                      'Project Desc': p_desc,
                      'Project Start': p_start,
                      'Project End': p_end,
                      'Project asign': p_asign,
                      'Project status': p_status,
                      'project_id': p_id
                    }
            print(queries)
            return v_data
        except Exception as e:
            v_data = {'Status':'Error Updating Task',
                      'Project Desc': p_desc,
                      'Project Start': p_start,
                      'Project End': p_end,
                      'Err Code': str(e)
                    }
            return v_data
    
    def getTaskID(p_id):
        try:
            cursor = conn.cursor()
            queries = queries_task.getTaskID(p_id)
            cursor.execute(queries)
            data = cursor.fetchone()
            retval = {'data': data}
            return retval
        except Exception as e:
            print(e)
            retval = {'Err gettask':str(e)
                    }
            return retval