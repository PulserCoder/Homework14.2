from flask import Blueprint
from system_of_database import SystemOfDatabaseDAO

movie_blueprint = Blueprint('movie', __name__)
DAO_Database = SystemOfDatabaseDAO()

@movie_blueprint.route('/movie/<title>')
def show_data_by_film(title):
    return DAO_Database.search_by_title(title)
