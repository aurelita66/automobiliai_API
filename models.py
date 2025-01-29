from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Automobilis(db.Model):
    __tablename__ = "automobilis"
    id = db.Column(db.Integer, primary_key=True)
    gamintojas = db.Column(db.String)
    modelis = db.Column(db.String)
    spalva = db.Column(db.String)
    metai = db.Column(db.Integer)

    @property
    def average_year(self):
        autos = self.query.all()
        res = round(sum(auto.metai for auto in autos) / len(autos))
        return res

    def __repr__(self):
        return f"id: {self.id} {self.gamintojas} {self.modelis} {self.spalva} {self.metai}"
