from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Team(db.Model):
    __tablename__ = 'Team'
    team_name = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('User.username'))

    def __init__(self, team_name, username):
        self.team_name = team_name
        self.username = username

class Player(db.Model):
    __tablename__ = 'Player'
    player_id = db.Column(db.Integer, primary_key=True)
    fantasy_team_name = db.Column(db.String(50), db.ForeignKey('Team.team_name'))