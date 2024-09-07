"""Database for Melon Tasting(Name of db is melon_tasting)."""

from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    email = db.Column(db.Integer, autoincrement=True, primary_key=True)

    appt =db.relationship("Appointment", back_populates="users")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"
    

class Appointment(db.Model):
    """Appointment information."""

    __tablename__ = "appointments"

    appt_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)

    user = db.relationship("User", back_populates="appointments")
    def __repr__(self):
        return f"Appointment app_id{self.appt_id} date={self.date}>"
    



    def connect_to_db(flask_app, db_uri="postgresql:///melong tasting", echo=True):
        flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        flask_app.config["SQLALCHEMY_ECHO"] = echo = False 
        flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        db.app = flask_app
        db.init_app(flask_app)

    print("Connected to the db!")
    if __name__=="__main__":
        from server import app

        connect_to_db(app)