from models import db, Automobilis
from flask import Flask, render_template, jsonify
from serializers import AutomobilisSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/api/automobiliai")
def api_automobiliai():
    all_autos = Automobilis.query.all()
    autos_data = [{
        "id": auto.id,
        "manufacturer": auto.gamintojas,
        "model": auto.modelis,
        "color": auto.spalva,
        "year": auto.metai
    } for auto in all_autos]
    return jsonify(autos_data)


@app.route("/api2/automobiliai")
def api2_automobiliai():
    all_autos = Automobilis.query.all()
    autos_data = [AutomobilisSchema.model_validate(auto).model_dump() for auto in all_autos]
    return jsonify(autos_data)


@app.route("/frontend")
def frontend():
    return render_template("automobiliai.html")


if __name__ == "__main__":
    app.run()
