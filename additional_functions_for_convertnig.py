from types_ import ResponseByRelease, ResponseByTitle, ResponseByRating
from exeptions import IncorrectResponse


class AdditionalForSearching:
    def _making_list_with_responses_by_release(self, data: list) -> list[ResponseByRelease]:
        ll = []
        for element in data:
            ll.append(ResponseByRelease(title=element[0],
                                        release_year=element[1]))
        if len(ll) < 1:
            raise IncorrectResponse
        return ll

    def _convert_to_json_by_date(self, data: list[ResponseByRelease]):
        data = self._making_list_with_responses_by_release(data)
        ll = []
        for element in data:
            ll.append({'title': element.title,
                       'release_year': element.release_year})
        return ll

    def _convert_to_json_by_title(self, data: ResponseByTitle) -> dict:
        return {
            "title": data.title,
            "country": data.county,
            "release_year": data.release_year,
            "genre": data.listed_in,
            "description": data.description}

    def _making_list_with_responses_by_rating(self, data: list) -> list[ResponseByRating]:
        ll = []
        for element in data:
            ll.append(ResponseByRating(title=element[0],
                                       rating=element[1],
                                       description=element[2]))
        if len(ll) < 1:
            raise IncorrectResponse
        return ll

    def _convert_to_json_by_rating(self, data: list) -> list[dict]:
        ll = []
        for element in self._making_list_with_responses_by_rating(data):
            ll.append({
                'title': element.title,
                'rating': element.rating,
                'description': element.description
            })
        if len(ll) < 1:
            raise IncorrectResponse
        return ll
