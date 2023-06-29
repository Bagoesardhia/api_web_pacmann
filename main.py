from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS

from connection.connection import conn

from modules.login.controllers.login_controller import logincontroller

from modules.task.controllers.task_controller import taskController


app = Flask(__name__)
CORS(app)

def output(id):
    cursor = conn.cursor()
    v_query = "SELECT cust_id, cust_first_name, cust_last_name FROM APPL.APPL_MST_CUSTOMERS where cust_id = %s"
    cursor.execute(v_query, (id,))
    data = cursor.fetchone()
    return data

def register_query(cust_id,first_name, last_name):
    try:
        cursor = conn.cursor()
        v_query = "INSERT INTO APPL.APPL_MST_CUSTOMERS (cust_id, cust_first_name, cust_last_name) VALUES (%s,%s,%s)"
        cursor.execute(v_query, (cust_id,first_name,last_name))
        conn.commit()
        return 0
    except Exception as e:
        data = 'Err insert data',e
        print(data)
        return data

def check_users(fn, ln):
    try:
        cursor = conn.cursor()
        v_query = "SELECT cust_first_name, cust_last_name FROM APPL.APPL_MST_CUSTOMERS where cust_first_name = %s and cust_last_name = %s"
        cursor.execute(v_query, (fn, ln))
        data = cursor.fetchone()
        if data == None:
            return 0
        else:
            return 1
    except Exception as e:
        data = 'err',e
        print(data)
        return 1

@app.route('/api', methods=['GET'])
def api():
    data = output()
    response = {'results': data}
    return jsonify(response)

@app.route('/api/id', methods=['GET'])
def check_id():
    id = request.args.get('id')
    data = output(id)

    if data != None:
        user_data = {'id':'ID Ditemukan',
                     'results': data
                     }
        print('con1',data)
        return jsonify(user_data)
    else:
        user_data = {'id':'ID Tidak Ditemukan'}
        print('con 2',id)
        return jsonify(user_data)

@app.route('/api/register', methods=['POST'])
def register():
    cust_id = request.form['cust_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    v_user = check_users(first_name, last_name)

    if v_user == 0:
        print (v_user)
        v_data = register_query(cust_id, first_name, last_name)
        if v_data == 0:
            return jsonify({'results':v_data,
                            'data':{
                                'first name': first_name,
                                'last name': last_name
                            }
                            })
        else:
            return jsonify({'results':'ID Already Exists'
                            })
    else:
        print (v_user)
        return jsonify({'results':'Name Already Exists'})    

## Modules Login
@app.route('/api/v1/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    data = logincontroller.main_login(username, password)
    response = {'results': data}
    return jsonify(response)

## Module Task

## GET ALL TASKS
@app.route('/task', methods=['GET'])
def getTask():
    data = taskController.main_task(p_type= 'A',
                                    p_project = None, 
                                    p_desc= None, 
                                    p_start= None, 
                                    p_end = None,
                                    p_createby = None, 
                                    p_createdate = None,
                                    p_updateby = None, 
                                    p_updatedate = None,
                                    p_id= None
                                    )
    response = {'results': data}
    return jsonify(data)

## INSERT TASK
@app.route('/task/new', methods=['POST'])
def insertTask():
    #id = request.form['id']
    #project = request.form['project']
    #desc = request.form['desc']
    #start = request.form['start']
    #end = request.form['end']
    #createdby = request.form['createdby']
    #data1 = request.get_json()
    #response = data['id','project','desc','start','end','createdby']
    #response = data1['id','project']
    id = request.get_json()['id']
    project = request.get_json()['project']
    desc = request.get_json()['desc']
    start = request.get_json()['start']
    end = request.get_json()['end']
    createdby = request.get_json()['createdby']
    #id = request.get_json('id')
    #project = request.get_json('project')
    #desc = request.get_json('desc')
    #start = request.get_json('start')
    #end = request.get_json('end')
    #createdby = request.get_json('createdby')
    current_date = datetime.now().strftime("%Y-%m-%d")
    data = taskController.main_task(p_type= 'N',
                                    p_id = id,
                                    p_project = project, 
                                    p_desc= desc, 
                                    p_start= start, 
                                    p_end = end,
                                    p_createby = createdby, 
                                    p_createdate = current_date,
                                    p_updateby = None ,
                                    p_updatedate = None)
    response = {'results': data}
    return jsonify(response)

## UPDATE TASK
@app.route('/task/update', methods=['POST'])
def updateTask():
    project = request.form['project']
    desc = request.form['desc']
    start = request.form['start']
    end = request.form['end']
    updateby = request.form['updateby']
    id = request.form['id']
    current_date = datetime.now().strftime("%Y-%m-%d")
    data = taskController.main_task(p_type= 'U',
                                    p_project = project, 
                                    p_desc= desc, 
                                    p_start= start, 
                                    p_end = end,
                                    p_createby = '', 
                                    p_createdate = '',
                                    p_updateby = updateby, 
                                    p_updatedate = current_date,
                                    p_id= id
                                    )
    response = {'results': data}
    return jsonify(response)



if __name__ == '__main__':
    app.run()