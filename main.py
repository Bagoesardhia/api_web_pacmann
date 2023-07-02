from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS

from connection.connection import conn

from modules.login.controllers.login_controller import logincontroller

from modules.task.controllers.task_controller import taskController

from modules.register.controllers.register_controller import registerController


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
    username = request.get_json()['username']
    password = request.get_json()['password']
    data = logincontroller.main_login(username, password)
    response = {'results': data}
    if data != 0:
        response = {'results': data}
        return jsonify(response), 401
    else:
        response = {'results': data,
                    'name': username
                    }
        return jsonify(response), 200


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
                                    p_id= None,
                                    p_owner = None, 
                                    p_asign = None, 
                                    p_status = None
                                    )
    response = {'results': data}
    return jsonify(data)

@app.route('/task/v1', methods=['GET'])
def getTaskv1():
    data = taskController.main_task(p_type= 'AN',
                                    p_project = None, 
                                    p_desc= None, 
                                    p_start= None, 
                                    p_end = None,
                                    p_createby = None, 
                                    p_createdate = None,
                                    p_updateby = None, 
                                    p_updatedate = None,
                                    p_id= None,
                                    p_owner = None, 
                                    p_asign = None, 
                                    p_status = None
                                    )
    response = {'results': data}
    return jsonify(data)

## INSERT TASK
@app.route('/task/new', methods=['POST'])
def insertTask():
    id = request.get_json()['id']
    project = request.get_json()['project']
    desc = request.get_json()['desc']
    start = request.get_json()['start']
    end = request.get_json()['end']
    createdby = request.get_json()['createdby']
    owner = request.get_json()['owner']
    asign = request.get_json()['asign']
    status = request.get_json()['status']
    
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
                                    p_updatedate = None,
                                    p_owner = owner, 
                                    p_asign = asign, 
                                    p_status = status)
    response = {'results': data}
    return jsonify(response)

## UPDATE TASK
@app.route('/task/update', methods=['POST'])
def updateTask():
    ## PARAMETERS QUERY
    id = request.get_json()['id']

    ## BODY
    desc = request.get_json()['desc']
    start = request.get_json()['start']
    end = request.get_json()['end']
    updateby = request.get_json()['updateby']
    asign = request.get_json()['asign']
    status = request.get_json()['status']

    current_date = datetime.now().strftime("%Y-%m-%d")

    data = taskController.main_task(p_type= 'U',
                                    p_project = '', 
                                    p_desc= desc, 
                                    p_start= start, 
                                    p_end = end,
                                    p_createby = '', 
                                    p_createdate = '',
                                    p_updateby = updateby, 
                                    p_updatedate = current_date,
                                    p_id= id,
                                    p_owner = "",
                                    p_asign = asign, 
                                    p_status = status
                                    )
    response = {'results': data}
    return jsonify(response)

## GET TASK BY ID
@app.route('/task/id', methods=['GET'])
def getTaskID():
    try:
        id = request.args.get('id')
        ##id = request.args.get('id')
        data = taskController.main_task(p_type= 'AD',
                                        p_project = '', 
                                        p_desc= '', 
                                        p_start= '', 
                                        p_end = '',
                                        p_createby = '', 
                                        p_createdate = '',
                                        p_updateby = '', 
                                        p_updatedate = '',
                                        p_id= id,
                                        p_owner = None, 
                                        p_asign = None, 
                                        p_status = None
                                        )
        print(id)
        response = {'results': data}
        return jsonify(response)
    except Exception as e:
        response = {'err main': str(e)}
        return jsonify(response)

## MODULES REGISTER

## GET ALL USERS
@app.route('/users', methods=['GET'])
def getUsers():
    data = registerController.main(p_type= 'A'
                                    )
    response = {'results': data}
    return jsonify(response)

## INSERT NEW USERS
@app.route('/users/register', methods=['POST'])
def newUsers():
    name = request.get_json()['name']
    username = request.get_json()['username']
    password = request.get_json()['password']
    role = request.get_json()['role']
    current_date = datetime.now().strftime("%Y-%m-%d")
    data = registerController.main(p_type = 'N', 
                                   p_name = name, 
                                   p_username = username, 
                                   p_password = password, 
                                   p_role = role, 
                                   p_created_by = 'ADMIN',
                                   p_created_date = current_date
                                    )
    response = {'results': data}
    return jsonify(response)



if __name__ == '__main__':
    app.run()