from flask import Flask ,url_for
app = Flask(__name__)


@app.route('/')          # input URL == http://127.0.0.1:5000/post/10
def hello_world():
    return 'Hi,i am here waiting for you !'

'''
@app.route('/post/<int:post_id>')   # input URL == http://127.0.0.1:5000/post/10
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
'''

'''
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():       # http://127.0.0.1:5000/post/10/login/user/John Doe
   print url_for('index')
   print url_for('login')
   print url_for('login', next='/')
   print url_for('profile', username='John Doe')
'''


'''
/
/login
/login?next=/
/user/John%20Doe
'''


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
