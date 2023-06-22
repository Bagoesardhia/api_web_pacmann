from flask import Flask, jsonify, request
from controllers.login_controller import login

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def api():
    user = request.form('username')
    pasw = request.form('password')
    data = login.check_users(user, pasw)
    response = {'results': data}
    return jsonify(response)

if __name__ == '__main__':
    app.run()