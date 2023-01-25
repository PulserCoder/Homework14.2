from typing import NamedTuple


class ResponseByTitle(NamedTuple):
    title: str
    county: str
    release_year: int
    listed_in: str
    description: str


class ResponseByRelease(NamedTuple):
    title: str
    release_year: int


class ResponseByRating(NamedTuple):
    title: str
    rating: str
    description: str