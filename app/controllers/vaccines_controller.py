from datetime import datetime, timedelta
from flask import jsonify, request, current_app
from app.models.vaccine_model import Vaccine

def post_vaccine():
    data = request.json

    if not data['cpf'].isnumeric() or len(data['cpf']) != 11:
        return '', 400

    first_shot_date = datetime.today()
    second_shot_date = datetime.today() + timedelta(+90)

    data['first_shot_date'] = first_shot_date
    data['second_shot_date'] = second_shot_date

    vaccine = Vaccine(**data)

    session = current_app.db.session

    session.add(vaccine)
    session.commit()

    return jsonify(vaccine), 201


def get_vaccines():
    vaccines_list = Vaccine.query.all()
    return jsonify(vaccines_list), 200
