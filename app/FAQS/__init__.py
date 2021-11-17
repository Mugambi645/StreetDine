from flask import Blueprint
faqs = Blueprint('faqs',__name__)
from . import views,forms,models