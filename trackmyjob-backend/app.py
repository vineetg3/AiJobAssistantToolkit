from flask import Flask,request,jsonify
from flask_restful import Api
from security import bcrypt,jwt
from resources.user import UserRegister,UserLogin,UserLogout
from resources.userJob import UserJobPost,UserJobList,UserJobById
from flask_sqlalchemy import SQLAlchemy
from database import db,migrate
from flask_cors import CORS
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_DATABASE_URI']=app.config['DATABASE_URI'].replace("s://", "sql://", 1)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={
        r"/*": {
            "origins": ["http://127.0.0.1:3000", "http://localhost:3000"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
        }
    })
    migrate.init_app(app, db)# this exposes some new flask terminal commands to us!
    return app

app=create_app()
api = Api(app)
api.add_resource(UserRegister, '/api/auth/signup')
api.add_resource(UserLogin, '/api/auth/login')
api.add_resource(UserLogout, '/api/auth/logout')
api.add_resource(UserJobPost, '/api/userjob')
api.add_resource(UserJobById, '/api/userjob/<int:pk>')
api.add_resource(UserJobList, '/api/userjobs')

@app.route("/")
def hello():
    return "TrackMyJob - API"

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    file = request.files['pdf']
    # Save the file in the current directory
    file.save(os.path.join('./resumes', file.filename))
    return jsonify({"message": "File uploaded successfully"}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)


 