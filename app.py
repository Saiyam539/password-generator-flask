from flask import Flask,render_template,request,flash
import random

app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def password():
    if request.form['lengths']:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = '0123456789'
        special = '!@#$%^&*'
        length  = int(request.form['lengths'])
        all = lower + upper + num + special
        random_password = "".join(random.sample(all,length))
        message = f"Your password is: {random_password}"
        flash(message)
        return render_template('index.html', password=message)
        
    else:
        message = 'Please enter a password length'
        flash(message)
        return render_template('index.html',password=message)


if __name__ == '__main__':
    app.run(debug=True)