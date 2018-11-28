from flask import Flask, jsonify, request, abort, make_response, Response, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def proces():
    if request.method == 'POST':
        print(" --------------_> ", request.form)
        name = request.form['owner']
        number = request.form['cardNumber']
        return render_template('process.html',name=name, card=number)
    return render_template('process.html')

if __name__ == '__main__':
    app.run(debug = True, ssl_context=('cert.pem', 'key.pem'))

