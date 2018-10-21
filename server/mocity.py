from flask import Flask
from flask import request

app = Flask(__name__)
app.run(host='0.0.0.0',port=80)

@app.route('/test', methods=['GET'])
def signin_form():
    return '''<form action="/" method="post">
              <h1>Welcome to Mo!</h1>
              <p><button type="submit" name="choice" value="in" >Im 硬</button></p>
              <p><button type="submit" name="choice" value="no" >run away</button></p>
              </form>'''

@app.route('/test', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['choice']=='in':
        return '<h3>nice</h3>'
    return '<h3>fuck yourself</h3>'


if __name__ == '__main__':
    app.run()