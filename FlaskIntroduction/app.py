from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Voeg deze regel toe

    def __repr__(self):
        return f"<Task {self.id}>"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "test.db")}'
db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        if not task_content.strip():
            return "Task content cannot be empty."
        new_task = Task(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task."


    else:
        tasks = Task.query.order_by(Task.id).all()  # Gebruik de juiste klasse en kolom
        return render_template('index.html', tasks=tasks)
        
@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    try:
        task_to_delete = Task.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue with deleting that task."
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue with updating the task."
    else:
      return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(port=8080, debug=True)