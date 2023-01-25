from flask import Blueprint, jsonify
from exeptions import IncorrectResponse
from system_of_database import SearchDATABASE

genre_rating = Blueprint('genre', __name__)


@genre_rating.route('/genre/<genre>')
def show_last_10_movies_by_genre(genre):
    database = SearchDATABASE()
    try:
        return jsonify(database.search_by_genre(genre))
    except IncorrectResponse:
        database.quit()
        return 'Bye, bye :('