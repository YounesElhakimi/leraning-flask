# save this as app.py
from flask import Flask , request , redirect , url_for , render_template

app = Flask(__name__ ,  template_folder={"template"})
app.config.from_object('config')

@app.route("/")
def hello():
    return "Hello, World!!"

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/user/<username>")
def show_user(username):
    return "Welcome {} !! ".format(username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "the post number is {}".format(post_id)


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "the path is : {}".format(subpath)


#get request
@app.route("/person")
def get_infoperson() :
    fn =  request.args.get("fn")
    ln =  request.args.get("ln")
    return "first name : {}  , last name : {}".format(fn , ln)









if __name__ == '__main__':
    app.run(port=app.config['PORT'],debug = app.config['DEBUG'])