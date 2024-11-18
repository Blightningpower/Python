from flask import Flask, request, render_template
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "Hello"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8080, debug=True)