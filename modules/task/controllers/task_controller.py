from connection.connection import conn

from ..models.queries_models import queries_task


class taskController():
    def main_task(p_project, p_desc, p_start, p_end):
        insertTask = taskController.insert_task(p_project, p_desc, p_start, p_end)
        if insertTask == 0:
            v_data = {'Status':'Task Berhasil Ditambahkan',
                      'Project Name': p_project,
                      'Project Desc': p_desc,
                      'Project Start': p_start,
                      'Project End': p_end,
                    }
            return v_data

    def check_task():
        None

    def insert_task(p_project, p_desc, p_start, p_end):
        try:
            cursor = conn.cursor()
            queries = queries_task.insertTask()
            cursor.execute(queries, (p_project, p_desc, p_start, p_end))
            conn.commit()
            return 0
        except Exception as e:
            data = 'error insert data task ', e
            return data
