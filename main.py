from flask import Flask, jsonify, request

from connection.connection import conn

from modules.login.controllers.login_controller import logincontroller

from modules.task.controllers.task_controller import taskController

app = Flask(__name__)

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

@app.route('/api/v1/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    data = logincontroller.main_login(username, password)
    response = {'results': data}
    return jsonify(response)

@app.route('/task', methods=['POST'])
def insertTask():
    project = request.form['project']
    desc = request.form['desc']
    start = request.form['start']
    end = request.form['end']
    data = taskController.main_task(project,desc,start,end)
    response = {'results': data}
    print(data)
    return jsonify(response)


if __name__ == '__main__':
    app.run()