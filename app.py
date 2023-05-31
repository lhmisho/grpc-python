from flask import Flask, request

from user_client import UserService
from message import Message
from greeting_client import GreetingService
app = Flask(__name__)


@app.route('/signup', methods=['POST'])
def sign_up():
    m = Message()
    username = request.json.get('user', "110")
    password = request.json.get('pass', "220")
    us = UserService()

    # sign up by using username and password
    res = us.sign_up(username, password)
    if res.status:
        m.status = True
        m.user_id = res.id
    return m.json()


@app.route('/greeting', methods=['POST'])
def greeting():
    m = Message()
    name = request.json.get('name')
    greeting = request.json.get('greeting')
    gr = GreetingService()
    res = gr.greeting(name, greeting)
    m.status = 200
    m.message = res
    return m.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8002", debug=True)
