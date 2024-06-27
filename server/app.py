#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<parameter>')
def count(parameter):
    return ''.join([str(i)+'\n' for i in range(int(parameter))])

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):

    if operation == '+':
        return str(num1+num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return f'Enter a valid operation'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
