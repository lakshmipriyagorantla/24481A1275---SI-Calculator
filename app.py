from flask import Flask , redirect , url_for , render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to Flaskapp<=>routing"

@app.route('/greet/<uname>')
def greet(uname):
    return f"Good Morning, {uname}!"

'''
@app.route('/delete/<int: roll>')
def delete_user(roll):
    return redirect(url_for('greet'))
'''

@app.route('/calculate' , methods=['GET', 'POST'])
def Si():
    if request.method == 'POST':
        P = float(request.form['p'])
        R = float(request.form['r'])
        T = float(request.form['t'])
        result = (P * R * T) / 100
        total = P + result
        return render_template('index.html', result=result, total=total, p=P, r=R, t=T)
    return render_template('index.html',)


if __name__ == '__main__':
    app.run(debug=True,port=3500)


