from flask import Blueprint, jsonify
from system_of_database import SearchDATABASE
from exeptions import IncorrectResponse

movie_blueprint = Blueprint('movie', __name__)

@movie_blueprint.route('/movie/<title>')
def show_data_by_film(title):
    try:
        DAO_Database = SearchDATABASE()
        result = DAO_Database.search_by_title(title)
        DAO_Database.quit()
        return jsonify(result)
    except IncorrectResponse:
        return "Bye, bye, we don't have this film"


@movie_blueprint.route('/movie/<int:year_d>/to/<int:year_u>')
def show_data_by_release_date_in_range(year_d: int, year_u: int):
    try:
        DAO_Database = SearchDATABASE()
        result = DAO_Database.search_in_range(year_d, year_u)
        DAO_Database.quit()
        return jsonify(result)
    except IncorrectResponse:
        return "Bye, bye, we don't have films in these dates"