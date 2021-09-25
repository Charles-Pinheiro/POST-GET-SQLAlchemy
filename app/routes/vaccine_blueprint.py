from flask import Blueprint
from app.controllers.vaccines_controller import post_vaccine, get_vaccines

bp = Blueprint('vaccine_bp', __name__, url_prefix='/vaccination')

bp.post('')(post_vaccine)
bp.get('')(get_vaccines)
