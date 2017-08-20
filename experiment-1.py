from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print 'index invoked'
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    print 'login invoked'
    pass

@app.route('/user/<username>', methods=['GET', 'POST'])
def profile(username):
    print 'profile invoked'
    return 'foo'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_with_template(name=None):
    print 'base url:{}, method:{}, path:{}'.format(request.base_url, request.method, request.path)
    return render_template('my-first-jinja-template.htm', name=name)

if __name__ == '__main__':
    with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login', next='/')
        print url_for('profile', username='John Doe')
        #   for static pages
        print url_for('static', filename='foo.html')
        #   use of templates
        print url_for('hello_with_template', name='robert')
    app.run()

