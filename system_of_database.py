import sqlite3
from typing import NamedTuple
from exeptions import IncorrectResponse


class ResponseByTitle(NamedTuple):
    title: str
    county: str
    release_year: int
    listed_in: str
    description: str


class SystemOfDatabaseDAO():
    def __init__(self):
        self.connection = sqlite3.connect('netflix.db')

    def quit(self):
        self.connection.close()

    def search_by_title(self, title_):
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title = ?
        ORDER BY release_year
        """
        cursor = self.connection.cursor()
        result = cursor.execute(query, (title_,)).fetchone()
        data = ResponseByTitle(title=result[0],
                               county=result[1],
                               release_year=result[2],
                               listed_in=result[3],
                               description=result[4])
        return self._convert_to_json_by_title(data)

    def _convert_to_json_by_title(self, data: ResponseByTitle):
        try:
            return {
                "title": data.title,
                "country": data.county,
                "release_year": data.release_year,
                "genre": data.listed_in,
                "description": data.description}
        except (ValueError, TypeError):
            raise IncorrectResponse


t = SystemOfDatabaseDAO()
t.search_by_title('3%')
