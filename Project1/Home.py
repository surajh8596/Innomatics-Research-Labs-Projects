from flask import Flask, request
app=Flask(__name__)

@app.route('/')
def home_page():
    return  "Welcome to First Backend Server created by Mr. Suraj\nTo Check your name is UpperCase go to '/upper'\nTo add, subtract, multiply or divide two numbers go to '/add', '/subtract', '/multiply', '/divide' Page Respectively."

@app.route('/upper')
def name_upper():
    name= request.args.get('name')
    return (f"Welcome {name.upper()}")

@app.route('/add')
def add_num():
    a=request.args.get('a')
    b=request.args.get('b')
    return (f"Addition of number {a} & {b} is {str(int(a)+int(b))}")

@app.route('/subtract')
def sub_num():
    a=request.args.get('a')
    b=request.args.get('b')
    return (f"Subtraction of number {a} & {b} is {str(int(a)-int(b))}")

@app.route('/multiply')
def mul_num():
    a=request.args.get('a')
    b=request.args.get('b')
    return (f"Multiplication of number {a} & {b} is {str(int(a)*int(b))}")

@app.route('/divide')
def div_num():
    a=request.args.get('a')
    b=request.args.get('b')
    return (f"Division of number {a} & {b} is {str(int(a)/int(b))}")

@app.route('/factorial')
def fact_num():
    num=request.args.get('num')
    import math
    fact=math.factorial(int(num))
    return (f"Factorial of number {num} is {str(fact)}")

if __name__ == '__main__':
    app.run(debug=True)
