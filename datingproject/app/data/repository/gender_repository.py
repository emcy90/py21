from app.data.db import session
from app.data.models import Gender
from app.controllers.gender_controller import *


def create_gender(gender_name):
    gender = Gender(Gender_name=gender_name)
    session.add(gender)
    session.commit()
