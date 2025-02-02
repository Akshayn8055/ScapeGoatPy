from flask import Flask, render_template, request, jsonify, Response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vuln1')
def missing_security_headers():
    return render_template('vuln1.html')

@app.route('/vuln2')
def no_xss_protection():
    return render_template('vuln2.html')

@app.route('/vuln3')
def missing_hsts():
    return render_template('vuln3.html')

@app.route('/vuln4')
def open_redirect():
    redirect_url = request.args.get('url', 'http://example.com')
    return redirect(redirect_url)

@app.route('/vuln5', methods=['POST'])
def weak_password():
    password = request.form.get('password')
    if password == '12345':
        return jsonify(message="Password is too weak!"), 400
    return jsonify(message="Password is strong!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
