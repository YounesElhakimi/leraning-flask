from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def show_index():
    posts = ['post 1 ' , 'post 2 ' , 'post 3' , 'post 4']
    return render_template('index.html' , posts = posts )

if __name__ == '__main__':
    app.run(debug=True)