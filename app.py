from flask import Flask
from app.movie_blueprint import movie_blueprint
from app.rating_blueprint import rating_blueprint
from app.genre_rating import genre_rating


app = Flask(__name__)
app.register_blueprint(movie_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(genre_rating)


if __name__ == '__main__':
    app.run()