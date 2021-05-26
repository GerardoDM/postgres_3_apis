import flask
from flask.app import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/demodb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class RobotModel(db.Model):
    __tablename__ = 'robot'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())

    def __init__(self,nombre):
        self.nombre = nombre
    
    def __repr__(self):
        return f"<Robot {self.nombre}>"

@app.route('/robots', methods=['POST', 'GET'])
def handle_robots():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            nuevo_robot = RobotModel(nombre=data['nombre'])
            db.session.add(nuevo_robot)
            db.session.commit()
            return {"message": f"robot {nuevo_robot.nombre} a sido creado exitosamente"}
        else:
            return {"error" : "The request payload is not in JSON format"}
    elif request.method == 'GET':
        robots = RobotModel.query.all()
        results = [{
            "id" : robot.id,
            "nombre" : robot.nombre 
        } for robot in robots]

        return {"count" : len(robots), "robots": results}


@app.route('/', methods=['GET'])
def index():
    return "<h3>Hello</h3>"


if __name__ == '__main__':
    app.run(debug=True)
