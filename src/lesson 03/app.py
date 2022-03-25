from flask import Flask , render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# js = Bundle('js/jquery.js', 'js/base.js', 'js/widgets.js', filters='jsmin', output='gen/packed.js')
# assets.register('js_all', js)

css = Bundle('css/common.css', 'css/admin.css', filters='cssmin', output='gen/packed.css')
assets.register('css_all', css)

@app.route('/')
@app.route('/index')
def show_index():
    posts = ['post 1 ' , 'post 2 ' , 'post 3' , 'post 4']
    return render_template('index.html' , posts = posts )

if __name__ == '__main__':
    app.run(debug=True)