from flask import Flask, render_template, request, redirect
from models.model import db
from models.model import Weather
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course.db'
db.init_app(app)

'''
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        location_object = Weather(longtitude=request.form['longtitude']
                                   ,latitude=request.form['latitude'],
                                   name=request.form['name'])
        try:
            db.session.add(location_object)
            db.session.commit()
            return redirect('/')
        except:
            return "DATABASE Errror"
    else:
        location_objects = Weather.query.order_by(Weather.date_created).all()
        return render_template('index.html',location_objects=location_objects)

@app.route('/createdatabase')
def CreateDatabase():
    
    import models
    with app.app_context():
        db.drop_all()
        db.create_all()
        return "Database Created"
    return "Something Wrong"
'''

if __name__ == "__main__":
    app.run(debug=True)
