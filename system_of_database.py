import sqlite3
from additional_functions_for_convertnig import AdditionalForSearching
from types_ import ResponseByTitle


class SystemOfDatabaseDAO():
    def __init__(self):
        self.connection = sqlite3.connect('netflix.db', check_same_thread=False)
        self.connection.row_factory = sqlite3.Row

    def quit(self):
        self.connection.close()


class SearchDATABASE(SystemOfDatabaseDAO):
    def __init__(self):
        super().__init__()

    def search_by_title(self, title_: str) -> dict:
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title = ?
        ORDER BY release_year
        """
        cursor = self.connection.cursor()
        result = cursor.execute(query, (title_,)).fetchone()
        try:
            data = ResponseByTitle(title=result[0],
                                   county=result[1],
                                   release_year=result[2],
                                   listed_in=result[3],
                                   description=result[4])
            return AdditionalForSearching()._convert_to_json_by_title(data)
        except (ValueError, TypeError):
            raise

    def search_in_range(self, year_d: int, year_u: int):
        query = """
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN ? AND ?
        LIMIT 100
        """
        cursor = self.connection.cursor()
        data = cursor.execute(query, (year_d, year_u,)).fetchall()
        return AdditionalForSearching()._convert_to_json_by_date(data)

    def search_by_rating(self, rating_list: tuple):
        query = f"""
        SELECT title, rating, description FROM netflix
        WHERE rating IN {rating_list}
        """
        cursor = self.connection.cursor()
        data = cursor.execute(query).fetchall()
        return AdditionalForSearching()._convert_to_json_by_rating(data)

    def search_by_genre(self, genre):
        query = """
        SELECT title, description FROM netflix
        WHERE listed_in = ?
        ORDER BY release_year DESC 
        LIMIT 10
        """
        cursor = self.connection.cursor()
        data = cursor.execute(query, (genre, )).fetchall()
        ll = []
        for element in data:
            ll.append({'title': element[0],
                       'description': element[1]})
        return ll

    def search_actors(self, first_name, second_name):
        query = """
        SELECT `cast`
        FROM netflix
        WHERE `cast` LIKE ?
        AND `cast` LIKE ?
        """
        cursor = self.connection.cursor()
        data = cursor.execute(query, ('%'+first_name+'%', '%'+second_name+'%', )).fetchall()
        sl = {}
        for i in data:
            for j in i:
                for h in j.split(', '):
                    if h in sl.keys():
                        sl[h] += 1
                    else:
                        sl[h] = 1
        for i in sl.items():
            if i[1] > 2:
                print(i[0])

    def get_pictures(self, type, genre, release_year):
        cursor = self.connection.cursor()
        query = """
        SELECT title, description
        FROM netflix
        WHERE type = ?
        AND listed_in = ?
        AND release_year = ?
        """
        ll = []
        for i in cursor.execute(query, (type, genre, release_year, )).fetchall():
            ll.append(
                {
                    'title': i[0],
                    'description': i[1]
                }
            )
        print(ll)
if __name__ == '__main__':
    sometest = SearchDATABASE()
    sometest.get_pictures('Movie', 'Dramas', '2020')