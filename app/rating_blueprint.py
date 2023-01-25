from flask import Blueprint, jsonify
from system_of_database import SearchDATABASE
from config import SortByRating
from exeptions import IncorrectResponse

rating_blueprint = Blueprint('rating', __name__)


@rating_blueprint.route('/rating/<type>')
def show_films_by_rating(type):
    database = SearchDATABASE()
    try:
        if type == 'family':
            return jsonify(database.search_by_rating(SortByRating.family))
        elif type == 'children':
            return jsonify(database.search_by_rating(SortByRating.children))
        elif type == 'adult':
            return jsonify(database.search_by_rating(SortByRating.adult))
        database.quit()
    except IncorrectResponse:
        database.quit()
        return 'Bye, bye, we have problem with this type'
