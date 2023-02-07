from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = ['111111111', '22222222', '33333333333']
@app.route("/")
def index():
    print(url_for('about'))
    print(url_for('index'))
    return render_template('index.html', title='Index', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='About', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return render_template('index.html', title=username, menu=menu)


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form['username'])
    return render_template('contact.html', title='Contact', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)



